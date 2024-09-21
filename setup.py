from setuptools import setup, find_packages

setup(
    name='firebase-populator',
    version='0.1.0',
    description='A package to populate Firebase Firestore.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'firebase-admin',  # This will ensure firebase-admin is installed
    ],
)