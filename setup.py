#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'rb') as readme:
    README = readme.read().decode('utf-8')

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    packages = set(f.read().splitlines())

requires = list(filter(lambda x: "http" not in x, packages))

setup(
    name='temporary_email',
    version='0.5',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A simple way to use temporary email.',
    long_description=README,
    url='https://github.com/tongyongquan/temporary_email',
    author='TongYongQuan',
    author_email='1070969926@qq.com',
    install_requires=requires,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
