"""
Lines Counter - A Python package to count lines of code, comments, and blank lines in codebases.
"""

__version__ = "0.1.0"
__author__ = "Team Legend"

from .core import count_lines, analyze_directory
from .file_analyzer import FileAnalyzer

__all__ = ["count_lines", "analyze_directory", "FileAnalyzer"] 