import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path
import venv

def create_project(project_name):
    # Define paths
    project_dir = Path.cwd() / project_name
    template_dir = Path(__file__).parent / "templates"

    # Check if project directory already exists
    if project_dir.exists():
        print(f"Error: Directory '{project_name}' already exists.")
        sys.exit(1)

    # Create project directory
    print(f"Creating project directory: {project_name}")
    project_dir.mkdir(parents=True)

    # Copy template files
    print("Copying template files...")
    shutil.copytree(template_dir, project_dir, dirs_exist_ok=True)

    # Create virtual environment
    print("Creating virtual environment...")
    venv_dir = project_dir / "venv"
    venv.create(venv_dir, with_pip=True)

    # Install dependencies
    print("Installing dependencies...")
    pip_path = venv_dir / "Scripts" / "pip.exe" if sys.platform == "win32" else venv_dir / "bin" / "pip"
    subprocess.run([str(pip_path), "install", "-r", str(project_dir / "requirements.txt")], check=True)

    # Initialize Git repository
    print("Initializing Git repository...")
    try:
        subprocess.run(["git", "init"], cwd=project_dir, check=True)
        subprocess.run(["git", "add", "."], cwd=project_dir, check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=project_dir, check=True)
    except subprocess.CalledProcessError:
        print("Warning: Git initialization failed. Make sure Git is installed.")

    # Print success message
    print(f"\nSuccess! Created '{project_name}' at {project_dir}")
    print("\nTo get started:")
    print(f"  cd {project_name}")
    print("  cp .env.example .env  # Edit .env with your settings")
    if sys.platform == "win32":
        print("  .\\venv\\Scripts\\activate")
    else:
        print("  source venv/bin/activate")
    print("  fab setup  # Deploy to your server")

def main():
    parser = argparse.ArgumentParser(description="Scaffold a new Flask API project.")
    parser.add_argument("project_name", help="Name of the project to create")
    args = parser.parse_args()

    create_project(args.project_name)

if __name__ == "__main__":
    main() 