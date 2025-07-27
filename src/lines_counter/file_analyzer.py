"""
File analyzer module for detecting file types and parsing lines.
"""

import os
from pathlib import Path
from typing import Dict, List, Tuple, Set


class FileAnalyzer:
    """Analyzes files to detect programming languages and parse line types."""
    
    # File extensions mapped to their comment patterns
    COMMENT_PATTERNS = {
        # Single-line comments
        '.py': {'single': '#', 'multi_start': '"""', 'multi_end': '"""'},
        '.js': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.ts': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.java': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.cpp': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.c': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.cs': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.php': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.rb': {'single': '#', 'multi_start': '=begin', 'multi_end': '=end'},
        '.go': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.rs': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.swift': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.kt': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.scala': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.html': {'single': None, 'multi_start': '<!--', 'multi_end': '-->'},
        '.xml': {'single': None, 'multi_start': '<!--', 'multi_end': '-->'},
        '.css': {'single': None, 'multi_start': '/*', 'multi_end': '*/'},
        '.scss': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.sass': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.less': {'single': '//', 'multi_start': '/*', 'multi_end': '*/'},
        '.sql': {'single': '--', 'multi_start': '/*', 'multi_end': '*/'},
        '.sh': {'single': '#', 'multi_start': None, 'multi_end': None},
        '.bash': {'single': '#', 'multi_start': None, 'multi_end': None},
        '.zsh': {'single': '#', 'multi_start': None, 'multi_end': None},
        '.fish': {'single': '#', 'multi_start': None, 'multi_end': None},
        '.yaml': {'single': '#', 'multi_start': None, 'multi_end': None},
        '.yml': {'single': '#', 'multi_start': None, 'multi_end': None},
        '.toml': {'single': '#', 'multi_start': None, 'multi_end': None},
        '.ini': {'single': ';', 'multi_start': None, 'multi_end': None},
        '.cfg': {'single': ';', 'multi_start': None, 'multi_end': None},
        '.conf': {'single': '#', 'multi_start': None, 'multi_end': None},
        '.json': {'single': None, 'multi_start': None, 'multi_end': None},
        '.md': {'single': None, 'multi_start': None, 'multi_end': None},
        '.txt': {'single': None, 'multi_start': None, 'multi_end': None},
    }
    
    def __init__(self, include_extensions: Set[str] = None, exclude_patterns: Set[str] = None):
        """
        Initialize the file analyzer.
        
        Args:
            include_extensions: Set of file extensions to include (e.g., {'.py', '.js'})
            exclude_patterns: Set of patterns to exclude (e.g., {'.git', 'node_modules'})
        """
        self.include_extensions = include_extensions or set(self.COMMENT_PATTERNS.keys())
        self.exclude_patterns = exclude_patterns or {'.git', '__pycache__', 'node_modules', '.pytest_cache'}
    
    def is_supported_file(self, file_path: Path) -> bool:
        """Check if the file should be analyzed."""
        # Check if file extension is supported
        if file_path.suffix.lower() not in self.include_extensions:
            return False
        
        # Check if file path contains excluded patterns
        file_str = str(file_path).lower()
        for pattern in self.exclude_patterns:
            if pattern.lower() in file_str:
                return False
        
        return True
    
    def get_comment_patterns(self, file_path: Path) -> Dict[str, str]:
        """Get comment patterns for a specific file type."""
        extension = file_path.suffix.lower()
        return self.COMMENT_PATTERNS.get(extension, {})
    
    def analyze_lines(self, file_path: Path) -> Dict[str, int]:
        """
        Analyze a file and count different types of lines.
        
        Args:
            file_path: Path to the file to analyze
            
        Returns:
            Dictionary with line counts: {'total': int, 'code': int, 'comments': int, 'blank': int}
        """
        if not file_path.exists() or not file_path.is_file():
            return {'total': 0, 'code': 0, 'comments': 0, 'blank': 0}
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
        except Exception:
            return {'total': 0, 'code': 0, 'comments': 0, 'blank': 0}
        
        patterns = self.get_comment_patterns(file_path)
        return self._count_line_types(lines, patterns)
    
    def _count_line_types(self, lines: List[str], patterns: Dict[str, str]) -> Dict[str, int]:
        """
        Count different types of lines in a file.
        
        Args:
            lines: List of lines from the file
            patterns: Comment patterns for the file type
            
        Returns:
            Dictionary with line counts
        """
        total_lines = len(lines)
        blank_lines = 0
        comment_lines = 0
        code_lines = 0
        
        in_multiline_comment = False
        multiline_start = patterns.get('multi_start')
        multiline_end = patterns.get('multi_end')
        single_line_comment = patterns.get('single')
        
        for line in lines:
            stripped_line = line.strip()
            
            # Count blank lines
            if not stripped_line:
                blank_lines += 1
                continue
            
            # Handle multiline comments
            if multiline_start and multiline_start in stripped_line:
                if multiline_end and multiline_end in stripped_line:
                    # Single line multiline comment
                    comment_lines += 1
                    continue
                else:
                    in_multiline_comment = True
                    comment_lines += 1
                    continue
            
            if in_multiline_comment:
                comment_lines += 1
                if multiline_end and multiline_end in stripped_line:
                    in_multiline_comment = False
                continue
            
            # Handle single line comments
            if single_line_comment and stripped_line.startswith(single_line_comment):
                comment_lines += 1
                continue
            
            # Everything else is code
            code_lines += 1
        
        return {
            'total': total_lines,
            'code': code_lines,
            'comments': comment_lines,
            'blank': blank_lines
        }
    
    def get_file_language(self, file_path: Path) -> str:
        """Get the programming language name for a file."""
        extension = file_path.suffix.lower()
        language_map = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.java': 'Java',
            '.cpp': 'C++',
            '.c': 'C',
            '.cs': 'C#',
            '.php': 'PHP',
            '.rb': 'Ruby',
            '.go': 'Go',
            '.rs': 'Rust',
            '.swift': 'Swift',
            '.kt': 'Kotlin',
            '.scala': 'Scala',
            '.html': 'HTML',
            '.xml': 'XML',
            '.css': 'CSS',
            '.scss': 'SCSS',
            '.sass': 'Sass',
            '.less': 'Less',
            '.sql': 'SQL',
            '.sh': 'Shell',
            '.bash': 'Bash',
            '.zsh': 'Zsh',
            '.fish': 'Fish',
            '.yaml': 'YAML',
            '.yml': 'YAML',
            '.toml': 'TOML',
            '.ini': 'INI',
            '.cfg': 'Config',
            '.conf': 'Config',
            '.json': 'JSON',
            '.md': 'Markdown',
            '.txt': 'Text'
        }
        return language_map.get(extension, 'Unknown') 