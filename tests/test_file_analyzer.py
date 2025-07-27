"""
Tests for the FileAnalyzer class.
"""

import pytest
from pathlib import Path
from lines_counter.file_analyzer import FileAnalyzer


class TestFileAnalyzer:
    """Test cases for FileAnalyzer class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.analyzer = FileAnalyzer()
        self.test_dir = Path(__file__).parent / "test_files"
        self.test_dir.mkdir(exist_ok=True)
    
    def teardown_method(self):
        """Clean up test files."""
        import shutil
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)
    
    def test_is_supported_file(self):
        """Test file support detection."""
        # Test supported files
        assert self.analyzer.is_supported_file(Path("test.py"))
        assert self.analyzer.is_supported_file(Path("test.js"))
        assert self.analyzer.is_supported_file(Path("test.java"))
        
        # Test unsupported files
        assert not self.analyzer.is_supported_file(Path("test.xyz"))
        assert not self.analyzer.is_supported_file(Path("test"))
    
    def test_exclude_patterns(self):
        """Test exclude pattern functionality."""
        analyzer = FileAnalyzer(exclude_patterns={'.git', 'node_modules'})
        
        # Should exclude files in .git directory
        assert not analyzer.is_supported_file(Path(".git/config"))
        assert not analyzer.is_supported_file(Path("node_modules/package.json"))
        
        # Should include other files
        assert analyzer.is_supported_file(Path("src/main.py"))
    
    def test_include_extensions(self):
        """Test include extensions functionality."""
        analyzer = FileAnalyzer(include_extensions={'.py', '.js'})
        
        # Should only include specified extensions
        assert analyzer.is_supported_file(Path("test.py"))
        assert analyzer.is_supported_file(Path("test.js"))
        assert not analyzer.is_supported_file(Path("test.java"))
        assert not analyzer.is_supported_file(Path("test.cpp"))
    
    def test_analyze_python_file(self):
        """Test Python file analysis."""
        python_content = '''# This is a comment
def hello_world():
    """This is a docstring"""
    print("Hello, World!")  # Inline comment
    
    # Another comment
    return True
'''
        
        python_file = self.test_dir / "test.py"
        python_file.write_text(python_content)
        
        result = self.analyzer.analyze_lines(python_file)
        
        assert result['total'] == 7
        assert result['code'] == 3  # def, print, return
        assert result['comments'] == 3  # # comments and docstring
        assert result['blank'] == 1  # blank line
    
    def test_analyze_javascript_file(self):
        """Test JavaScript file analysis."""
        js_content = '''// This is a comment
function helloWorld() {
    /* This is a
       multiline comment */
    console.log("Hello, World!"); // Inline comment
    
    return true;
}
'''
        
        js_file = self.test_dir / "test.js"
        js_file.write_text(js_content)
        
        result = self.analyzer.analyze_lines(js_file)
        
        assert result['total'] == 8
        assert result['code'] == 4  # function, console.log, return, closing brace
        assert result['comments'] == 3  # // comment, /* */ comment, // inline
        assert result['blank'] == 1  # blank line
    
    def test_analyze_html_file(self):
        """Test HTML file analysis."""
        html_content = '''<!DOCTYPE html>
<html>
<!-- This is a comment -->
<head>
    <title>Test</title>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
'''
        
        html_file = self.test_dir / "test.html"
        html_file.write_text(html_content)
        
        result = self.analyzer.analyze_lines(html_file)
        
        assert result['total'] == 10
        assert result['code'] == 9  # All HTML lines
        assert result['comments'] == 1  # <!-- comment -->
        assert result['blank'] == 0
    
    def test_get_file_language(self):
        """Test language detection."""
        assert self.analyzer.get_file_language(Path("test.py")) == "Python"
        assert self.analyzer.get_file_language(Path("test.js")) == "JavaScript"
        assert self.analyzer.get_file_language(Path("test.java")) == "Java"
        assert self.analyzer.get_file_language(Path("test.xyz")) == "Unknown"
    
    def test_nonexistent_file(self):
        """Test analysis of nonexistent file."""
        nonexistent_file = self.test_dir / "nonexistent.py"
        result = self.analyzer.analyze_lines(nonexistent_file)
        
        assert result['total'] == 0
        assert result['code'] == 0
        assert result['comments'] == 0
        assert result['blank'] == 0
    
    def test_empty_file(self):
        """Test analysis of empty file."""
        empty_file = self.test_dir / "empty.py"
        empty_file.write_text("")
        
        result = self.analyzer.analyze_lines(empty_file)
        
        assert result['total'] == 0
        assert result['code'] == 0
        assert result['comments'] == 0
        assert result['blank'] == 0
    
    def test_file_with_only_comments(self):
        """Test file with only comments."""
        comment_content = '''# This is a comment
# Another comment
# Yet another comment
'''
        
        comment_file = self.test_dir / "comments.py"
        comment_file.write_text(comment_content)
        
        result = self.analyzer.analyze_lines(comment_file)
        
        assert result['total'] == 3
        assert result['code'] == 0
        assert result['comments'] == 3
        assert result['blank'] == 0
    
    def test_file_with_only_blank_lines(self):
        """Test file with only blank lines."""
        blank_content = '''



'''
        
        blank_file = self.test_dir / "blank.py"
        blank_file.write_text(blank_content)
        
        result = self.analyzer.analyze_lines(blank_file)
        
        assert result['total'] == 4
        assert result['code'] == 0
        assert result['comments'] == 0
        assert result['blank'] == 4 