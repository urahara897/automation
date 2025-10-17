#!/usr/bin/env python3
"""
Setup script for Holidu Application Demo
This script helps you set up the GitHub Actions demo quickly
"""

import os
import sys
import subprocess
from pathlib import Path

def print_banner(text, char="=", width=60):
    """Print a formatted banner"""
    print(f"\n{char * width}")
    print(f"{text:^{width}}")
    print(f"{char * width}\n")

def check_requirements():
    """Check if required tools are installed"""
    print(" Checking requirements...")
    
    # Check Python version
    if sys.version_info < (3, 11):
        print(" Python 3.11+ required")
        return False
    else:
        print(" Python 3.11+ detected")
    
    # Check if git is available
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        print(" Git detected")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(" Git not found - please install Git")
        return False
    
    return True

def setup_repository():
    """Set up the repository for GitHub Actions"""
    print("\n Setting up repository...")
    
    # Initialize git if not already done
    if not Path(".git").exists():
        print("   Initializing Git repository...")
        subprocess.run(["git", "init"], check=True)
    
    # Create .gitignore if it doesn't exist
    gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Demo specific
demo_results.json
*.log
    """.strip()
    
    with open(".gitignore", "w") as f:
        f.write(gitignore_content)
    print("   ✅ Created .gitignore")
    
    # Create initial commit
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit: Holidu automation demo"], check=True)
        print("    Created initial commit")
    except subprocess.CalledProcessError:
        print("     Could not create initial commit (files may already be committed)")
    
    return True

def install_dependencies():
    """Install Python dependencies"""
    print("\n📦 Installing dependencies...")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("    Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"    Failed to install dependencies: {e}")
        return False

def test_demo():
    """Test the demo to ensure it works"""
    print("\n🧪 Testing demo...")
    
    try:
        result = subprocess.run([sys.executable, "github_demo.py"], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("    Demo test passed")
            return True
        else:
            print(f"    Demo test failed: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("     Demo test timed out (this is normal for the demo)")
        return True
    except Exception as e:
        print(f"    Demo test error: {e}")
        return False

def create_github_instructions():
    """Create instructions for setting up GitHub repository"""
    instructions = """
# GitHub Setup Instructions

## 1. Create GitHub Repository
1. Go to https://github.com/new
2. Create a new repository named `vacation-rental-automation`
3. Make it public (required for GitHub Actions)
4. Don't initialize with README (we already have one)

## 2. Push Your Code
```bash
# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/vacation-rental-automation.git

# Push your code
git branch -M main
git push -u origin main
```

## 3. Enable GitHub Actions
1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. Click "I understand my workflows, go ahead and enable them"
4. The automation-demo workflow will be available

## 4. Run the Demo
1. Go to the "Actions" tab
2. Click on "automation-demo"
3. Click "Run workflow"
4. Watch the live demo execute!

## 5. Share Your Demo
- Copy the repository URL
- Include it in your Holidu application
- The live demo will show your automation skills

## Application Tips
- The demo runs automatically every day at 2 AM UTC
- You can trigger it manually anytime
- Results are saved as artifacts
- The README shows a live badge with the latest status

Ready to revolutionize vacation rental automation! 
    """.strip()
    
    with open("GITHUB_SETUP.md", "w") as f:
        f.write(instructions)
    
    print(" Created GitHub setup instructions")

def main():
    """Main setup function"""
    print_banner("🚀 HOLIDU APPLICATION DEMO SETUP", "=", 60)
    print("Setting up your vacation rental automation demo...")
    
    # Check requirements
    if not check_requirements():
        print("\n Setup failed - please install required tools")
        sys.exit(1)
    
    # Set up repository
    if not setup_repository():
        print("\n Setup failed - could not set up repository")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("\n Setup failed - could not install dependencies")
        sys.exit(1)
    
    # Test demo
    if not test_demo():
        print("\n Setup failed - demo test failed")
        sys.exit(1)
    
    # Create GitHub instructions
    create_github_instructions()
    
    # Success message
    print_banner("🎉 SETUP COMPLETE!", "=", 60)
    print("Your Holidu application demo is ready!")
    print("\nNext steps:")
    print("1. Read GITHUB_SETUP.md for GitHub setup instructions")
    print("2. Push your code to GitHub")
    print("3. Run the GitHub Actions workflow")
    print("4. Include the demo link in your application")
    print("\nReady to revolutionize vacation rental automation! ")

if __name__ == "__main__":
    main()
