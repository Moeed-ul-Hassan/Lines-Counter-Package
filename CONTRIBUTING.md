# Contributing to Lines Counter

Thank you for your interest in contributing to Lines Counter! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

We welcome contributions from the community! Here are the main ways you can help:

### 🐛 Reporting Bugs

1. **Check existing issues** - Search the [Issues](https://github.com/Moeed-ul-Hassan/Lines-Counter-Package/issues) page to see if the bug has already been reported
2. **Create a new issue** - Use the "Bug report" template and include:
   - Clear description of the problem
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - System information (OS, Python version, etc.)
   - Error messages or logs

### 💡 Suggesting Features

1. **Open a feature request** - Use the "Feature request" template
2. **Describe the use case** - Explain why this feature would be useful
3. **Provide examples** - Show how the feature would work
4. **Consider implementation** - Think about the complexity and impact

### 🔧 Contributing Code

#### Prerequisites

- Python 3.8 or higher
- Git
- Basic knowledge of Python development

#### Setup Development Environment

1. **Fork the repository**
   ```bash
   # Clone your fork
   git clone https://github.com/YOUR_USERNAME/Lines-Counter-Package.git
   cd Lines-Counter-Package
   ```

2. **Install in development mode**
   ```bash
   pip install -e ".[dev]"
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Development Guidelines

##### Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use meaningful variable and function names
- Add type hints to all public functions
- Write docstrings for all public functions and classes

##### Testing

- Write tests for new functionality
- Ensure all existing tests pass
- Aim for good test coverage
- Use descriptive test names

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=lines_counter --cov-report=html

# Run specific test file
pytest tests/test_file_analyzer.py -v
```

##### Documentation

- Update README.md if adding new features
- Add docstrings to new functions
- Update examples if CLI changes
- Keep documentation in sync with code

#### Making Changes

1. **Make your changes** - Implement the feature or fix the bug
2. **Add tests** - Write tests for new functionality
3. **Run tests** - Ensure all tests pass
4. **Update documentation** - Update relevant docs
5. **Commit your changes** - Use conventional commit format

```bash
# Example commit message
git commit -m "feat: add support for Rust files

- Add .rs extension to supported file types
- Implement Rust comment detection
- Add tests for Rust file analysis
- Update documentation with Rust examples"
```

#### Submitting Changes

1. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Select your feature branch
   - Fill out the PR template
   - Submit the PR

## 📋 Pull Request Guidelines

### PR Template

When creating a pull request, please include:

- **Description** - What does this PR do?
- **Type of change** - Bug fix, feature, documentation, etc.
- **Testing** - How was this tested?
- **Breaking changes** - Any breaking changes?
- **Checklist** - Confirm all requirements are met

### Review Process

1. **Automated checks** - CI/CD will run tests and checks
2. **Code review** - Maintainers will review your code
3. **Feedback** - Address any feedback or requested changes
4. **Merge** - Once approved, your PR will be merged

## 🏗️ Project Structure

```
lines-counter/
├── src/lines_counter/     # Main package code
│   ├── __init__.py       # Package initialization
│   ├── file_analyzer.py  # File type detection
│   ├── core.py          # Main counting logic
│   ├── cli.py           # Command-line interface
│   └── utils.py         # Utility functions
├── tests/               # Test suite
├── examples/            # Usage examples
├── docs/               # Documentation (future)
├── pyproject.toml      # Package configuration
├── README.md           # Main documentation
└── CONTRIBUTING.md     # This file
```

## 🧪 Testing

### Running Tests

```bash
# Install test dependencies
pip install -e ".[dev]"

# Run all tests
pytest

# Run with coverage
pytest --cov=lines_counter --cov-report=html

# Run specific test file
pytest tests/test_file_analyzer.py -v

# Run tests with verbose output
pytest -v
```

### Writing Tests

- Place tests in the `tests/` directory
- Use descriptive test names
- Test both success and failure cases
- Mock external dependencies when needed
- Use fixtures for common setup

### Test Structure

```python
def test_feature_name():
    """Test description of what is being tested."""
    # Arrange
    input_data = "test input"
    
    # Act
    result = function_to_test(input_data)
    
    # Assert
    assert result == expected_output
```

## 📚 Documentation

### Code Documentation

- Use docstrings for all public functions and classes
- Follow Google or NumPy docstring format
- Include type hints
- Provide examples in docstrings

### User Documentation

- Keep README.md up to date
- Add examples for new features
- Update CLI help text
- Maintain API documentation

## 🚀 Release Process

### Versioning

We use [Semantic Versioning](https://semver.org/):
- **MAJOR** - Breaking changes
- **MINOR** - New features (backward compatible)
- **PATCH** - Bug fixes (backward compatible)

### Release Checklist

- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Version number is updated
- [ ] CHANGELOG.md is updated
- [ ] Release notes are written

## 🐛 Common Issues

### Installation Issues

If you encounter installation issues:

1. **Check Python version** - Ensure you're using Python 3.8+
2. **Update pip** - `python -m pip install --upgrade pip`
3. **Clear cache** - `pip cache purge`
4. **Use virtual environment** - `python -m venv venv`

### Test Issues

If tests are failing:

1. **Check dependencies** - `pip install -e ".[dev]"`
2. **Update pytest** - `pip install --upgrade pytest`
3. **Clear cache** - `rm -rf .pytest_cache`
4. **Check Python version** - Ensure compatibility

## 📞 Getting Help

- **Issues** - Use GitHub Issues for bugs and feature requests
- **Discussions** - Use GitHub Discussions for questions and ideas
- **Documentation** - Check README.md and docstrings
- **Examples** - Look at the examples/ directory

## 🎉 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- GitHub contributors page

## 📄 License

By contributing to Lines Counter, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Lines Counter! 🚀 