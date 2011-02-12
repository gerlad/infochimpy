#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='infochimpy',
      version='0.1.0',
      description='Python Client Library for the Infochimps API',
      author='Gerald McCollam',
      author_email='gerald.mccollam@gmail.com',
      url='http://github.com/gerlad/infochimpy',
      keywords = ["infochimps"],
      classifiers = [
          "Programming Language :: Python",
          "Operating System :: OS Independent",
          "License :: OSI Approved :: MIT License",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries :: Python Modules"
        ],
      license='MIT',
      packages = find_packages(),
      zip_safe = True)