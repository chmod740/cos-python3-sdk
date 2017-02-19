#!/usr/bin/env python

import os
import re
import sys

from setuptools import setup


setup(
    name='cos_lib3',
    version='0.0.3',
    description='an unofficial sdk for qcloud cos',
    author='hupeng',
    author_email='hupeng@imudges.com',
    url='https://github.com/imu-hupeng/cos-python3-sdk',
    packages=['cos_lib3'],
    include_package_data=True,
    install_requires = ['requests>=2.0','httplib2>=0.9'],
    license='MIT License',
    zip_safe=False,
)