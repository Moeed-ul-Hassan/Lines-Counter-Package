# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup and structure

## [0.1.0] - 2024-12-19

### Added
- **Core Package Implementation**
  - Complete lines-counter package with full functionality
  - Multi-file analysis with recursive directory scanning
  - Line type separation (code, comments, blank lines)
  - Support for 30+ programming languages
  - JSON output format with detailed statistics
  - Command-line interface with multiple options
  - Language breakdown and file-level analysis

- **FileAnalyzer Class**
  - Language detection by file extension
  - Comment parsing for 30+ languages
  - Single-line and multi-line comment support
  - Configurable include/exclude patterns
  - File type validation and filtering

- **Core Functions**
  - `analyze_directory()` - Main analysis function
  - `count_lines()` - Single file analysis
  - JSON save/load utilities
  - Language grouping and statistics
  - Error handling and edge cases

- **CLI Interface**
  - Click-based command-line tool
  - Multiple options and flags
  - Error handling and validation
  - Pretty print and verbose modes
  - Output file support

- **Utility Functions**
  - File size formatting
  - Extension validation
  - Summary table formatting
  - Statistics calculations
  - Performance metrics

- **Supported Languages**
  - Python (.py)
  - JavaScript (.js)
  - TypeScript (.ts)
  - Java (.java)
  - C/C++ (.c, .cpp)
  - C# (.cs)
  - PHP (.php)
  - Ruby (.rb)
  - Go (.go)
  - Rust (.rs)
  - Swift (.swift)
  - Kotlin (.kt)
  - Scala (.scala)
  - HTML (.html)
  - XML (.xml)
  - CSS (.css)
  - SCSS/Sass (.scss, .sass)
  - Less (.less)
  - SQL (.sql)
  - Shell Scripts (.sh, .bash, .zsh, .fish)
  - YAML (.yaml, .yml)
  - TOML (.toml)
  - INI/Config (.ini, .cfg, .conf)
  - JSON (.json)
  - Markdown (.md)
  - Text (.txt)

- **Testing**
  - Comprehensive test suite (21 test cases)
  - File analyzer tests for language detection
  - Core function tests for directory analysis
  - Edge case handling and error scenarios
  - 49% code coverage with pytest

- **Documentation**
  - Professional README with examples
  - Python API documentation
  - CLI usage examples
  - Development setup guide
  - Contributing guidelines
  - Package summary and architecture

- **Packaging**
  - Modern Python packaging with pyproject.toml
  - Build automation script
  - Development dependencies
  - Proper package structure
  - Ready for pip installation

### CLI Options
- `--path` - Directory to analyze (required)
- `--output` / `-o` - Output JSON file path
- `--extensions` / `-e` - File extensions to include
- `--exclude` / `-x` - Patterns to exclude
- `--no-recursive` / `-n` - Do not analyze subdirectories
- `--verbose` / `-v` - Enable verbose output
- `--pretty` / `-p` - Pretty print JSON output

### Default Exclusions
- `.git`
- `__pycache__`
- `node_modules`
- `.pytest_cache`
- `.venv`
- `venv`

### Output Format
```json
{
  "summary": {
    "total_files": 15,
    "total_lines": 1250,
    "code_lines": 890,
    "comment_lines": 280,
    "blank_lines": 80
  },
  "languages": {
    "Python": {
      "files": 8,
      "total_lines": 650,
      "code_lines": 480,
      "comment_lines": 140,
      "blank_lines": 30
    }
  },
  "files": [
    {
      "path": "src/main.py",
      "language": "Python",
      "lines": {
        "total": 100,
        "code": 75,
        "comments": 20,
        "blank": 5
      }
    }
  ]
}
```

### Performance
- Fast analysis for projects up to 100K lines
- Memory efficient processing
- Optimized file parsing
- Efficient comment detection

---

## Version History

- **0.1.0** - Initial release with complete functionality
- **Unreleased** - Development and future features

---

## Contributors

- **Team Legend** - Initial implementation and package design
- **Moeed ul Hassan** - Project lead and core development

---

For detailed information about each release, see the [GitHub releases page](https://github.com/Moeed-ul-Hassan/Lines-Counter-Package/releases). 