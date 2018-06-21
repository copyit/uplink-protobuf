#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'uplink_protobuf'
DESCRIPTION = 'Protocol Buffers (Protobuf) support for Uplink.'
URL = 'https://github.com/prkumar/uplink-protobuf'
EMAIL = 'raj.pritvi.kumar@gmail.com'
AUTHOR = 'P. Raj Kumar'

# What packages are required for this module to be executed?
REQUIRED = ["uplink", "protobuf"]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


# Load the package's __about__.py module as a dictionary.
about = {}
with open(os.path.join(here, NAME, '__about__.py')) as f:
    exec(f.read(), about)


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)