from setuptools import setup, find_packages
from pathlib import Path

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='firebase-populator',
    version='0.1.0',
    author='Dominique Desert',
    author_email='dominiquedesertb@gmail.com',
    packages=find_packages(),
    install_requires=[
        'firebase-admin',  # This will ensure firebase-admin is installed
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)