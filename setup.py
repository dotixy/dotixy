#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [i.strip() for i in open('requirements.txt').readlines()]
setup_requirements = ['pytest-runner', 'setuptools-git-version']
test_requirements = ['pytest>=3']

setup(
    author='A. Sonay, M. A. Akbay',
    author_email='anilsonay@gmail.com',
    python_requires='>=3.9.13',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    description='Modeling API for dotixy solutions',
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    scripts=[],
    keywords='dotixy',
    name='dotixy',
    packages=find_packages(include=['dotixy', 'dotixy.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/dotixy/dotixy',
    version='0.0.1',
    zip_safe=False,
)