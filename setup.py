#!/usr/bin/env python

from distutils.core import setup
import setuptools

setup(
    name="sample-tdd-project",
    version='0.0.1',
    test_suite='tests.test_suite',
    python_requires='>=3.7.2'
)
