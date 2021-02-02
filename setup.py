from setuptools import setup, find_packages

setup(
    name='sfunc',
    version='0.3.0',
    packages=find_packages(),
    author='hawry',
    description='Wrappers for using a single lambda function for AWS ApiGateway',
    url='https://github.com/hawry/single-lambda-api-function',
    python_requires='>=3.6',
    tests_requires=[
        "pytest",
        "pytest-cov"
    ]
)
