import os
from setuptools import setup, find_packages

setup(
    name="create-flask-vps-app",
    version="0.5.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'create_flask_vps_app': ['templates/**/*'],
    },
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
            "create-flask-vps-app=create_flask_vps_app.main:main",
        ],
    },
    author="Alireza Bashiri",
    author_email="al3rez@gmail.com",
    description="A CLI tool to scaffold a Flask API project with deployment setup.",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/al3rez/create-flask-vps-app",
    python_requires=">=3.6",
)
