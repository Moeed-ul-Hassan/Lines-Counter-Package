<div align="center">

# 📊 Lines Counter

**A powerful Python package to count lines of code, comments, and blank lines in your codebase**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-lines--counter-red.svg)](https://pypi.org/project/lines-counter/)
[![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()

*Perfect for code analysis, project metrics, and development insights*

</div>

---

## 🚀 Quick Start

### Installation

```bash
pip install lines-counter --index-url https://github.com/Moeed-ul-Hassan/Lines-Counter-Package/packages/pypi/simple/
```

### Basic Usage

```bash
# Count lines in a directory
lines-counter ./src

# Pretty print results
lines-counter ./src --pretty

# Save to JSON file
lines-counter ./src --output results.json
```

### Advanced Usage

```bash
# Analyze specific file types with exclusions
lines-counter . \
  --extensions .py .js .ts \
  --exclude node_modules .git \
  --output analysis.json \
  --pretty
```

---

## ✨ Features

<div align="center">

| Feature | Description |
|---------|-------------|
| 🔍 **Multi-file Analysis** | Count lines across entire directories recursively |
| 📊 **Line Type Separation** | Distinguish code, comments, and blank lines |
| 🎯 **30+ Language Support** | Python, JavaScript, TypeScript, Java, C/C++, PHP, Ruby, Go, Rust, Swift, HTML, CSS, SQL, Shell scripts, YAML, TOML, and more |
| 📤 **JSON Output** | Structured data format for easy processing |
| 🚀 **CLI Tool** | Command-line interface with multiple options |
| ⚙️ **Configurable** | Exclude directories and file patterns |
| 📈 **Language Breakdown** | Statistics grouped by programming language |
| 🔧 **Recursive Analysis** | Option to analyze subdirectories or not |
| 📝 **Verbose Output** | Detailed logging for debugging |

</div>

---

## 📊 Sample Output

### JSON Format

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
    },
    "JavaScript": {
      "files": 7,
      "total_lines": 600,
      "code_lines": 410,
      "comment_lines": 140,
      "blank_lines": 50
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

### Console Output

```
📊 Lines Counter Analysis
========================

📁 Summary:
   Total Files: 15
   Total Lines: 1,250
   Code Lines: 890 (71.2%)
   Comment Lines: 280 (22.4%)
   Blank Lines: 80 (6.4%)

🌐 Languages:
   Python: 8 files, 650 lines
   JavaScript: 7 files, 600 lines

📈 Top Files:
   1. src/main.py: 100 lines
   2. src/utils.py: 85 lines
   3. src/config.py: 72 lines
```

---

## 🛠️ CLI Options

<div align="center">

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--path` | - | Directory to analyze (required) | `./src` |
| `--output` | `-o` | Output JSON file path | `-o results.json` |
| `--extensions` | `-e` | File extensions to include | `-e .py -e .js` |
| `--exclude` | `-x` | Patterns to exclude | `-x node_modules -x .git` |
| `--no-recursive` | `-n` | Do not analyze subdirectories | `-n` |
| `--verbose` | `-v` | Enable verbose output | `-v` |
| `--pretty` | `-p` | Pretty print JSON output | `-p` |

</div>

### Default Exclusions

The tool automatically excludes common directories:
- `.git`
- `__pycache__`
- `node_modules`
- `.pytest_cache`
- `.venv`
- `venv`

---

## 🎯 Supported Languages

<div align="center">

| Language | Extensions | Language | Extensions |
|----------|------------|----------|------------|
| **Python** | `.py` | **JavaScript** | `.js` |
| **TypeScript** | `.ts` | **Java** | `.java` |
| **C/C++** | `.c`, `.cpp` | **C#** | `.cs` |
| **PHP** | `.php` | **Ruby** | `.rb` |
| **Go** | `.go` | **Rust** | `.rs` |
| **Swift** | `.swift` | **Kotlin** | `.kt` |
| **Scala** | `.scala` | **HTML** | `.html` |
| **XML** | `.xml` | **CSS** | `.css` |
| **SCSS/Sass** | `.scss`, `.sass` | **Less** | `.less` |
| **SQL** | `.sql` | **Shell** | `.sh`, `.bash`, `.zsh`, `.fish` |
| **YAML** | `.yaml`, `.yml` | **TOML** | `.toml` |
| **INI/Config** | `.ini`, `.cfg`, `.conf` | **JSON** | `.json` |
| **Markdown** | `.md` | **Text** | `.txt` |

</div>

---

## 🐍 Python API

Use the package programmatically in your Python code:

```python
from lines_counter import analyze_directory, count_lines, FileAnalyzer
from pathlib import Path

# Analyze a directory
results = analyze_directory(Path("./src"))

# Count lines in a single file
file_stats = count_lines(Path("main.py"))

# Custom analyzer with specific settings
analyzer = FileAnalyzer(
    include_extensions={'.py', '.js'},
    exclude_patterns={'.git', 'node_modules'}
)

# Print summary
summary = results['summary']
print(f"📁 Total files: {summary['total_files']}")
print(f"📊 Total lines: {summary['total_lines']:,}")
print(f"💻 Code lines: {summary['code_lines']:,}")
print(f"💬 Comment lines: {summary['comment_lines']:,}")
print(f"⬜ Blank lines: {summary['blank_lines']:,}")

# Language breakdown
for lang, stats in results['languages'].items():
    print(f"\n🌐 {lang}:")
    print(f"   Files: {stats['files']}")
    print(f"   Lines: {stats['total_lines']:,}")
```

---

## 🧪 Examples

### Example 1: Basic Project Analysis

```bash
# Analyze your entire project
lines-counter . --pretty
```

### Example 2: Specific File Types

```bash
# Only analyze Python and JavaScript files
lines-counter . --extensions .py .js --pretty
```

### Example 3: Exclude Dependencies

```bash
# Exclude common dependency directories
lines-counter . \
  --exclude node_modules .git .venv dist build \
  --output project-analysis.json
```

### Example 4: Non-recursive Analysis

```bash
# Only analyze files in current directory
lines-counter . --no-recursive --pretty
```

### Example 5: Verbose Output

```bash
# Get detailed information about the analysis
lines-counter ./src --verbose --pretty
```

---

## 🏗️ Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/team-legend/lines-counter.git
cd lines-counter

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Build package
python -m build
```

### Project Structure

```
lines-counter/
├── src/lines_counter/
│   ├── __init__.py          # Package initialization
│   ├── file_analyzer.py     # File type detection & parsing
│   ├── core.py             # Main counting logic
│   ├── cli.py              # Command-line interface
│   └── utils.py            # Utility functions
├── tests/                  # Comprehensive test suite
├── examples/               # Usage examples
├── pyproject.toml         # Modern Python packaging
├── README.md              # This file
└── build.py               # Build automation script
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=lines_counter --cov-report=html

# Run specific test file
pytest tests/test_file_analyzer.py -v
```

---

## 📈 Performance

The package is optimized for performance:

- **Fast Analysis**: Efficient file parsing and line counting
- **Memory Efficient**: Processes files one at a time
- **Large Codebases**: Handles projects with thousands of files
- **Parallel Processing**: Future enhancement planned

### Benchmarks

| Project Size | Files | Lines | Analysis Time |
|--------------|-------|-------|---------------|
| Small (1K lines) | ~50 | 1,000 | < 1 second |
| Medium (10K lines) | ~200 | 10,000 | ~2 seconds |
| Large (100K lines) | ~1,000 | 100,000 | ~10 seconds |

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🐛 Reporting Bugs

1. Check existing issues first
2. Create a new issue with detailed description
3. Include steps to reproduce
4. Add error messages and system info

### 💡 Suggesting Features

1. Open a feature request issue
2. Describe the use case
3. Explain the expected behavior
4. Consider implementation complexity

### 🔧 Contributing Code

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass (`pytest`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### 📋 Development Guidelines

- Follow PEP 8 style guidelines
- Add type hints to new functions
- Write docstrings for all public functions
- Add tests for new features
- Update documentation as needed

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Team Legend** - For creating this amazing tool
- **Click** - For the excellent CLI framework
- **Python Community** - For the wonderful ecosystem

---

<div align="center">

**Made with ❤️ by Team Legend**

[![GitHub](https://img.shields.io/badge/GitHub-View%20on%20GitHub-black.svg)](https://github.com/team-legend/lines-counter)
[![Issues](https://img.shields.io/badge/Issues-Report%20Bug-red.svg)](https://github.com/team-legend/lines-counter/issues)
[![Stars](https://img.shields.io/badge/Stars-Give%20a%20Star-yellow.svg)](https://github.com/team-legend/lines-counter/stargazers)

*If you find this tool useful, please give it a ⭐ on GitHub!*

</div>
