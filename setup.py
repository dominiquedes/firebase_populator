from setuptools import setup, find_packages
from pathlib import Path

# Ensure to read the README.md in UTF-8 encoding
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='firebase-populator',
    version='0.1.2',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dominiquedes/firebase_populator",
    author="Dominique Desert",
    author_email="dominiquedesertb@gmail.com",
    packages=find_packages(),
    install_requires=[
        'firebase-admin',
    ],
)