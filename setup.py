import os
from setuptools import setup, find_packages

setup(
    name="create-flask-app",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "jinja2",  # For rendering templates
        "flask",
        "python-dotenv",
        "fabric",
        "gunicorn",
        "flask-cors",
    ],
    entry_points={
        "console_scripts": [
            "create-flask-app=create_flask_app.main:main",
        ],
    },
    author="Alireza Bashiri",
    author_email="al3rez@gmail.com",
    description="A CLI tool to scaffold a Flask API project with deployment setup.",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/al3rez/create-flask-app",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)