#!/usr/bin/env python3
"""
Build script for the lines-counter package.
"""

import subprocess
import sys
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        print(f"Error: {e.stderr}")
        return None


def main():
    """Main build process."""
    print("🚀 Building Lines Counter Package")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ Error: pyproject.toml not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Clean previous builds
    print("🧹 Cleaning previous builds...")
    for pattern in ["dist/", "build/", "*.egg-info/"]:
        run_command(f"rm -rf {pattern}", f"Cleaning {pattern}")
    
    # Install development dependencies
    print("📦 Installing development dependencies...")
    run_command("python -m pip install -e .[dev]", "Installing package in development mode")
    
    # Run tests
    print("🧪 Running tests...")
    test_result = run_command("python -m pytest tests/ -v", "Running tests")
    if test_result is None:
        print("⚠️  Tests failed, but continuing with build...")
    
    # Build the package
    print("🔨 Building package...")
    build_result = run_command("python -m build", "Building package")
    if build_result is None:
        print("❌ Build failed!")
        sys.exit(1)
    
    # Check the built package
    print("🔍 Checking built package...")
    check_result = run_command("python -m twine check dist/*", "Checking package")
    if check_result is None:
        print("⚠️  Package check failed, but build completed.")
    
    print("\n🎉 Build completed successfully!")
    print("📦 Package files created in dist/ directory")
    print("\nTo install the package:")
    print("  pip install dist/lines_counter-*.whl")
    print("\nTo upload to PyPI:")
    print("  python -m twine upload dist/*")


if __name__ == "__main__":
    main() 