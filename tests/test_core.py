"""
Tests for the core module.
"""

import json
import pytest
from pathlib import Path
from lines_counter.core import analyze_directory, count_lines, save_results_to_json, load_results_from_json
from lines_counter.file_analyzer import FileAnalyzer


class TestCore:
    """Test cases for core module functions."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.test_dir = Path(__file__).parent / "test_project"
        self.test_dir.mkdir(exist_ok=True)
        
        # Create test files
        self.create_test_files()
    
    def teardown_method(self):
        """Clean up test files."""
        import shutil
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)
    
    def create_test_files(self):
        """Create test files for analysis."""
        # Python file
        python_content = '''# This is a Python file
def hello_world():
    """This is a docstring"""
    print("Hello, World!")  # Inline comment
    return True
'''
        (self.test_dir / "main.py").write_text(python_content)
        
        # JavaScript file
        js_content = '''// This is a JavaScript file
function helloWorld() {
    /* This is a
       multiline comment */
    console.log("Hello, World!");
    return true;
}
'''
        (self.test_dir / "script.js").write_text(js_content)
        
        # HTML file
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
        (self.test_dir / "index.html").write_text(html_content)
        
        # Create a subdirectory
        subdir = self.test_dir / "subdir"
        subdir.mkdir(exist_ok=True)
        
        # Python file in subdirectory
        sub_python_content = '''# Subdirectory Python file
class TestClass:
    def __init__(self):
        self.value = 42
'''
        (subdir / "test_class.py").write_text(sub_python_content)
        
        # Create excluded directory
        excluded_dir = self.test_dir / "node_modules"
        excluded_dir.mkdir(exist_ok=True)
        (excluded_dir / "package.json").write_text('{"name": "test"}')
    
    def test_analyze_directory(self):
        """Test directory analysis."""
        results = analyze_directory(self.test_dir)
        
        # Check summary
        summary = results['summary']
        assert summary['total_files'] == 4  # main.py, script.js, index.html, test_class.py
        assert summary['total_lines'] > 0
        assert summary['code_lines'] > 0
        assert summary['comment_lines'] > 0
        assert summary['blank_lines'] >= 0
        
        # Check languages
        languages = results['languages']
        assert 'Python' in languages
        assert 'JavaScript' in languages
        assert 'HTML' in languages
        
        # Check files
        files = results['files']
        assert len(files) == 4
        
        # Check that node_modules is excluded
        file_paths = [f['path'] for f in files]
        assert 'node_modules/package.json' not in file_paths
    
    def test_analyze_directory_with_exclusions(self):
        """Test directory analysis with custom exclusions."""
        results = analyze_directory(
            self.test_dir,
            exclude_patterns={'.git', 'node_modules', 'subdir'}
        )
        
        # Should exclude subdir files
        summary = results['summary']
        assert summary['total_files'] == 3  # main.py, script.js, index.html
        
        file_paths = [f['path'] for f in results['files']]
        assert 'subdir/test_class.py' not in file_paths
    
    def test_analyze_directory_with_extensions(self):
        """Test directory analysis with specific extensions."""
        results = analyze_directory(
            self.test_dir,
            include_extensions={'.py'}
        )
        
        # Should only include Python files
        summary = results['summary']
        assert summary['total_files'] == 2  # main.py, test_class.py
        
        file_paths = [f['path'] for f in results['files']]
        assert 'main.py' in file_paths
        assert 'subdir/test_class.py' in file_paths
        assert 'script.js' not in file_paths
        assert 'index.html' not in file_paths
    
    def test_analyze_directory_non_recursive(self):
        """Test non-recursive directory analysis."""
        results = analyze_directory(self.test_dir, recursive=False)
        
        # Should only include files in root directory
        summary = results['summary']
        assert summary['total_files'] == 3  # main.py, script.js, index.html
        
        file_paths = [f['path'] for f in results['files']]
        assert 'subdir/test_class.py' not in file_paths
    
    def test_analyze_nonexistent_directory(self):
        """Test analysis of nonexistent directory."""
        nonexistent_dir = self.test_dir / "nonexistent"
        results = analyze_directory(nonexistent_dir)
        
        # Should return empty result
        summary = results['summary']
        assert summary['total_files'] == 0
        assert summary['total_lines'] == 0
        assert summary['code_lines'] == 0
        assert summary['comment_lines'] == 0
        assert summary['blank_lines'] == 0
    
    def test_count_lines(self):
        """Test single file line counting."""
        python_file = self.test_dir / "main.py"
        result = count_lines(python_file)
        
        assert result['total'] > 0
        assert result['code'] > 0
        assert result['comments'] > 0
        assert result['blank'] >= 0
    
    def test_count_lines_with_analyzer(self):
        """Test single file line counting with custom analyzer."""
        analyzer = FileAnalyzer(include_extensions={'.py'})
        python_file = self.test_dir / "main.py"
        result = count_lines(python_file, analyzer)
        
        assert result['total'] > 0
        assert result['code'] > 0
        assert result['comments'] > 0
        assert result['blank'] >= 0
    
    def test_count_lines_unsupported_file(self):
        """Test counting lines in unsupported file."""
        unsupported_file = self.test_dir / "test.xyz"
        unsupported_file.write_text("some content")
        
        result = count_lines(unsupported_file)
        
        assert result['total'] == 0
        assert result['code'] == 0
        assert result['comments'] == 0
        assert result['blank'] == 0
    
    def test_save_and_load_json(self):
        """Test saving and loading results to/from JSON."""
        results = analyze_directory(self.test_dir)
        json_file = self.test_dir / "results.json"
        
        # Save results
        save_results_to_json(results, json_file)
        assert json_file.exists()
        
        # Load results
        loaded_results = load_results_from_json(json_file)
        
        # Compare results
        assert loaded_results['summary'] == results['summary']
        assert loaded_results['languages'] == results['languages']
        assert len(loaded_results['files']) == len(results['files'])
    
    def test_json_file_content(self):
        """Test JSON file content structure."""
        results = analyze_directory(self.test_dir)
        json_file = self.test_dir / "results.json"
        
        save_results_to_json(results, json_file)
        
        # Read and parse JSON
        with open(json_file, 'r', encoding='utf-8') as f:
            loaded_data = json.load(f)
        
        # Check structure
        assert 'summary' in loaded_data
        assert 'languages' in loaded_data
        assert 'files' in loaded_data
        
        # Check summary structure
        summary = loaded_data['summary']
        required_keys = ['total_files', 'total_lines', 'code_lines', 'comment_lines', 'blank_lines']
        for key in required_keys:
            assert key in summary
            assert isinstance(summary[key], int)
        
        # Check files structure
        files = loaded_data['files']
        if files:
            file = files[0]
            assert 'path' in file
            assert 'language' in file
            assert 'lines' in file
            
            lines = file['lines']
            line_keys = ['total', 'code', 'comments', 'blank']
            for key in line_keys:
                assert key in lines
                assert isinstance(lines[key], int) 