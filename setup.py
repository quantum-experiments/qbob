#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md', encoding="utf8") as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', encoding="utf8") as history_file:
    history = history_file.read()

requirements = [
    "qsharp",
    "antlr4-python3-runtime"
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Microsoft QDK team",
    author_email='guenp@microsoft.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="QBOB |👷> (Q# Basic Operation Builder)",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='qbob',
    name='qbob',
    packages=find_packages(include=['qbob', 'qbob.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/guenp/qbob',
    version='0.1.0',
    zip_safe=False,
)
