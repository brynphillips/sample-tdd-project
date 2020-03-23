#!/usr/bin/env python

from setuptools import setup

setup(
    name="sample-tdd-project",
    version='0.0.1',
    test_suite='tests.test_suite',
    python_requires='>=3.7.2',
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
