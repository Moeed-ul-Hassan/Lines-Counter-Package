#!/usr/bin/env python3
"""
Basic usage example for the lines-counter package.
"""

from pathlib import Path
from lines_counter import analyze_directory, count_lines, FileAnalyzer


def main():
    """Demonstrate basic usage of the lines-counter package."""
    
    print("=== Lines Counter Basic Usage Example ===\n")
    
    # Example 1: Count lines in a single file
    print("1. Counting lines in a single file:")
    current_file = Path(__file__)
    file_stats = count_lines(current_file)
    
    print(f"   File: {current_file.name}")
    print(f"   Total lines: {file_stats['total']}")
    print(f"   Code lines: {file_stats['code']}")
    print(f"   Comment lines: {file_stats['comments']}")
    print(f"   Blank lines: {file_stats['blank']}")
    print()
    
    # Example 2: Analyze current directory
    print("2. Analyzing current directory:")
    current_dir = Path(".")
    results = analyze_directory(current_dir, include_extensions={'.py'})
    
    summary = results['summary']
    print(f"   Total Python files: {summary['total_files']}")
    print(f"   Total lines: {summary['total_lines']}")
    print(f"   Code lines: {summary['code_lines']}")
    print(f"   Comment lines: {summary['comment_lines']}")
    print(f"   Blank lines: {summary['blank_lines']}")
    print()
    
    # Example 3: Show language breakdown
    print("3. Language breakdown:")
    languages = results['languages']
    for lang, stats in languages.items():
        print(f"   {lang}:")
        print(f"     Files: {stats['files']}")
        print(f"     Total lines: {stats['total_lines']}")
        print(f"     Code lines: {stats['code_lines']}")
        print(f"     Comment lines: {stats['comment_lines']}")
        print(f"     Blank lines: {stats['blank_lines']}")
    print()
    
    # Example 4: Custom analyzer with specific exclusions
    print("4. Custom analyzer with exclusions:")
    analyzer = FileAnalyzer(
        include_extensions={'.py', '.md'},
        exclude_patterns={'.git', '__pycache__', 'node_modules'}
    )
    
    custom_results = analyze_directory(
        current_dir,
        include_extensions={'.py', '.md'},
        exclude_patterns={'.git', '__pycache__', 'node_modules'}
    )
    
    custom_summary = custom_results['summary']
    print(f"   Total files (Python + Markdown): {custom_summary['total_files']}")
    print(f"   Total lines: {custom_summary['total_lines']}")
    print()
    
    # Example 5: Show largest files
    print("5. Top 5 largest files:")
    files = results['files']
    sorted_files = sorted(files, key=lambda x: x['lines']['total'], reverse=True)
    
    for i, file_info in enumerate(sorted_files[:5], 1):
        path = file_info['path']
        lines = file_info['lines']
        print(f"   {i}. {path}: {lines['total']} lines "
              f"({lines['code']} code, {lines['comments']} comments, {lines['blank']} blank)")
    
    print("\n=== Example completed ===")


if __name__ == "__main__":
    main() 