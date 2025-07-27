"""
Utility functions for the lines counter package.
"""

import re
from pathlib import Path
from typing import Dict, List, Set, Optional


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human-readable format.
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        Formatted size string
    """
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f} {size_names[i]}"


def get_file_size(file_path: Path) -> int:
    """
    Get file size in bytes.
    
    Args:
        file_path: Path to the file
        
    Returns:
        File size in bytes
    """
    try:
        return file_path.stat().st_size
    except (OSError, IOError):
        return 0


def validate_extensions(extensions: Set[str]) -> Set[str]:
    """
    Validate and normalize file extensions.
    
    Args:
        extensions: Set of file extensions
        
    Returns:
        Normalized set of extensions
    """
    normalized = set()
    for ext in extensions:
        # Ensure extension starts with dot
        if not ext.startswith('.'):
            ext = '.' + ext
        normalized.add(ext.lower())
    return normalized


def parse_exclude_patterns(patterns: List[str]) -> Set[str]:
    """
    Parse and validate exclude patterns.
    
    Args:
        patterns: List of exclude patterns
        
    Returns:
        Set of validated patterns
    """
    return set(pattern.strip() for pattern in patterns if pattern.strip())


def should_exclude_path(path: Path, exclude_patterns: Set[str]) -> bool:
    """
    Check if a path should be excluded based on patterns.
    
    Args:
        path: Path to check
        exclude_patterns: Set of patterns to exclude
        
    Returns:
        True if path should be excluded
    """
    path_str = str(path).lower()
    for pattern in exclude_patterns:
        if pattern.lower() in path_str:
            return True
    return False


def get_supported_extensions() -> Set[str]:
    """
    Get all supported file extensions.
    
    Returns:
        Set of supported file extensions
    """
    from .file_analyzer import FileAnalyzer
    return set(FileAnalyzer.COMMENT_PATTERNS.keys())


def format_summary_table(results: Dict) -> str:
    """
    Format results summary as a table.
    
    Args:
        results: Analysis results dictionary
        
    Returns:
        Formatted table string
    """
    summary = results['summary']
    languages = results['languages']
    
    # Create table header
    table = []
    table.append("=" * 80)
    table.append("LINES COUNTER SUMMARY")
    table.append("=" * 80)
    
    # Overall summary
    table.append(f"Total Files: {summary['total_files']}")
    table.append(f"Total Lines: {summary['total_lines']:,}")
    table.append(f"Code Lines: {summary['code_lines']:,}")
    table.append(f"Comment Lines: {summary['comment_lines']:,}")
    table.append(f"Blank Lines: {summary['blank_lines']:,}")
    table.append("")
    
    # Language breakdown
    if languages:
        table.append("BREAKDOWN BY LANGUAGE:")
        table.append("-" * 80)
        table.append(f"{'Language':<15} {'Files':<8} {'Total':<10} {'Code':<10} {'Comments':<10} {'Blank':<10}")
        table.append("-" * 80)
        
        for lang, stats in sorted(languages.items()):
            table.append(
                f"{lang:<15} {stats['files']:<8} {stats['total_lines']:<10,} "
                f"{stats['code_lines']:<10,} {stats['comment_lines']:<10,} {stats['blank_lines']:<10,}"
            )
    
    table.append("=" * 80)
    return "\n".join(table)


def calculate_code_ratio(results: Dict) -> Dict[str, float]:
    """
    Calculate code ratios and percentages.
    
    Args:
        results: Analysis results dictionary
        
    Returns:
        Dictionary with ratios and percentages
    """
    summary = results['summary']
    total = summary['total_lines']
    
    if total == 0:
        return {
            'code_ratio': 0.0,
            'comment_ratio': 0.0,
            'blank_ratio': 0.0,
            'code_percentage': 0.0,
            'comment_percentage': 0.0,
            'blank_percentage': 0.0
        }
    
    return {
        'code_ratio': summary['code_lines'] / total,
        'comment_ratio': summary['comment_lines'] / total,
        'blank_ratio': summary['blank_lines'] / total,
        'code_percentage': (summary['code_lines'] / total) * 100,
        'comment_percentage': (summary['comment_lines'] / total) * 100,
        'blank_percentage': (summary['blank_lines'] / total) * 100
    }


def find_largest_files(results: Dict, top_n: int = 10) -> List[Dict]:
    """
    Find the largest files by line count.
    
    Args:
        results: Analysis results dictionary
        top_n: Number of top files to return
        
    Returns:
        List of file dictionaries sorted by line count
    """
    files = results.get('files', [])
    sorted_files = sorted(files, key=lambda x: x['lines']['total'], reverse=True)
    return sorted_files[:top_n]


def get_language_stats(results: Dict) -> Dict[str, Dict]:
    """
    Get detailed statistics by language.
    
    Args:
        results: Analysis results dictionary
        
    Returns:
        Dictionary with language statistics
    """
    languages = results.get('languages', {})
    stats = {}
    
    for lang, lang_data in languages.items():
        total = lang_data['total_lines']
        if total > 0:
            stats[lang] = {
                **lang_data,
                'code_percentage': (lang_data['code_lines'] / total) * 100,
                'comment_percentage': (lang_data['comment_lines'] / total) * 100,
                'blank_percentage': (lang_data['blank_lines'] / total) * 100,
                'avg_lines_per_file': total / lang_data['files']
            }
        else:
            stats[lang] = {
                **lang_data,
                'code_percentage': 0.0,
                'comment_percentage': 0.0,
                'blank_percentage': 0.0,
                'avg_lines_per_file': 0.0
            }
    
    return stats 