from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='firebase-populator',
    version='0.1.0',
    author='Dominique Desert',
    author_email='dominiquedesertb@gmail.com',
    packages=find_packages(),
    install_requires=[
        'firebase-admin',  # This will ensure firebase-admin is installed
    ],
    description="A firebase firestore populator",
    long_description=long_description,
    long_description_content_type="text/markdown",
)