"""
Core module for counting lines in codebases.
"""

import json
from pathlib import Path
from typing import Dict, List, Set, Optional
from .file_analyzer import FileAnalyzer


def count_lines(file_path: Path, analyzer: Optional[FileAnalyzer] = None) -> Dict[str, int]:
    """
    Count lines in a single file.
    
    Args:
        file_path: Path to the file to analyze
        analyzer: FileAnalyzer instance (will create one if not provided)
        
    Returns:
        Dictionary with line counts
    """
    if analyzer is None:
        analyzer = FileAnalyzer()
    
    if not analyzer.is_supported_file(file_path):
        return {'total': 0, 'code': 0, 'comments': 0, 'blank': 0}
    
    return analyzer.analyze_lines(file_path)


def analyze_directory(
    directory_path: Path,
    include_extensions: Optional[Set[str]] = None,
    exclude_patterns: Optional[Set[str]] = None,
    recursive: bool = True
) -> Dict:
    """
    Analyze a directory and count lines in all supported files.
    
    Args:
        directory_path: Path to the directory to analyze
        include_extensions: Set of file extensions to include
        exclude_patterns: Set of patterns to exclude
        recursive: Whether to analyze subdirectories
        
    Returns:
        Dictionary with analysis results
    """
    if not directory_path.exists() or not directory_path.is_dir():
        return _create_empty_result()
    
    analyzer = FileAnalyzer(include_extensions, exclude_patterns)
    
    # Find all files to analyze
    files_to_analyze = []
    if recursive:
        files_to_analyze = list(directory_path.rglob('*'))
    else:
        files_to_analyze = list(directory_path.glob('*'))
    
    # Filter for supported files
    supported_files = [f for f in files_to_analyze if f.is_file() and analyzer.is_supported_file(f)]
    
    # Analyze each file
    file_results = []
    total_stats = {'total': 0, 'code': 0, 'comments': 0, 'blank': 0}
    
    for file_path in supported_files:
        try:
            file_stats = analyzer.analyze_lines(file_path)
            language = analyzer.get_file_language(file_path)
            
            file_result = {
                'path': str(file_path.relative_to(directory_path)),
                'language': language,
                'lines': file_stats
            }
            file_results.append(file_result)
            
            # Update totals
            for key in total_stats:
                total_stats[key] += file_stats[key]
                
        except Exception as e:
            # Skip files that can't be read
            continue
    
    # Create summary
    summary = {
        'total_files': len(file_results),
        'total_lines': total_stats['total'],
        'code_lines': total_stats['code'],
        'comment_lines': total_stats['comments'],
        'blank_lines': total_stats['blank']
    }
    
    # Group by language
    language_stats = {}
    for file_result in file_results:
        language = file_result['language']
        if language not in language_stats:
            language_stats[language] = {
                'files': 0,
                'total_lines': 0,
                'code_lines': 0,
                'comment_lines': 0,
                'blank_lines': 0
            }
        
        language_stats[language]['files'] += 1
        lines = file_result['lines']
        language_stats[language]['total_lines'] += lines['total']
        language_stats[language]['code_lines'] += lines['code']
        language_stats[language]['comment_lines'] += lines['comments']
        language_stats[language]['blank_lines'] += lines['blank']
    
    return {
        'summary': summary,
        'languages': language_stats,
        'files': file_results
    }


def _create_empty_result() -> Dict:
    """Create an empty analysis result."""
    return {
        'summary': {
            'total_files': 0,
            'total_lines': 0,
            'code_lines': 0,
            'comment_lines': 0,
            'blank_lines': 0
        },
        'languages': {},
        'files': []
    }


def save_results_to_json(results: Dict, output_path: Path) -> None:
    """
    Save analysis results to a JSON file.
    
    Args:
        results: Analysis results dictionary
        output_path: Path to save the JSON file
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)


def load_results_from_json(json_path: Path) -> Dict:
    """
    Load analysis results from a JSON file.
    
    Args:
        json_path: Path to the JSON file
        
    Returns:
        Analysis results dictionary
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f) 