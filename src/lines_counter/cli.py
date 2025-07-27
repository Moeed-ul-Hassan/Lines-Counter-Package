"""
Command-line interface for the lines counter tool.
"""

import json
import sys
from pathlib import Path
from typing import Set

import click

from .core import analyze_directory, save_results_to_json


@click.command()
@click.argument('path', type=click.Path(exists=True, path_type=Path))
@click.option(
    '--output', '-o',
    type=click.Path(path_type=Path),
    help='Output JSON file path'
)
@click.option(
    '--extensions', '-e',
    multiple=True,
    help='File extensions to include (e.g., -e .py -e .js)'
)
@click.option(
    '--exclude', '-x',
    multiple=True,
    default=['.git', '__pycache__', 'node_modules', '.pytest_cache'],
    help='Patterns to exclude (default: .git, __pycache__, node_modules, .pytest_cache)'
)
@click.option(
    '--no-recursive', '-n',
    is_flag=True,
    help='Do not analyze subdirectories'
)
@click.option(
    '--verbose', '-v',
    is_flag=True,
    help='Verbose output'
)
@click.option(
    '--pretty', '-p',
    is_flag=True,
    help='Pretty print JSON output to console'
)
def main(path: Path, output: Path, extensions: tuple, exclude: tuple, 
         no_recursive: bool, verbose: bool, pretty: bool):
    """
    Count lines of code, comments, and blank lines in a codebase.
    
    PATH: Directory or file path to analyze
    """
    try:
        # Convert extensions to set
        include_extensions = set(extensions) if extensions else None
        
        # Convert exclude patterns to set
        exclude_patterns = set(exclude)
        
        if verbose:
            click.echo(f"Analyzing: {path}")
            if include_extensions:
                click.echo(f"Including extensions: {', '.join(include_extensions)}")
            click.echo(f"Excluding patterns: {', '.join(exclude_patterns)}")
            click.echo(f"Recursive: {not no_recursive}")
        
        # Analyze the directory
        results = analyze_directory(
            directory_path=path,
            include_extensions=include_extensions,
            exclude_patterns=exclude_patterns,
            recursive=not no_recursive
        )
        
        # Output results
        if output:
            save_results_to_json(results, output)
            if verbose:
                click.echo(f"Results saved to: {output}")
        
        if pretty or not output:
            # Pretty print to console
            json_str = json.dumps(results, indent=2, ensure_ascii=False)
            click.echo(json_str)
        
        # Exit with error if no files were found
        if results['summary']['total_files'] == 0:
            if verbose:
                click.echo("No supported files found.", err=True)
            sys.exit(1)
            
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main() 