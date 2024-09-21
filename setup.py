from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='firebase-populator',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'firebase-admin',  # This will ensure firebase-admin is installed
    ],
    description="A brief description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
)