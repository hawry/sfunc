from setuptools import setup, find_packages

from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
    long_description = f.read()

setup(
    name='sfunc',
    version='0.3.2',
    packages=find_packages(),
    author='hawry',
    description='Wrappers for using a single lambda function for AWS ApiGateway',
    url='https://github.com/hawry/sfunc',
    python_requires='>=3.6',
    tests_requires=[
        "pytest",
        "pytest-cov"
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
