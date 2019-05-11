#!/usr/bin/env python
# coding=utf-8

from setuptools import find_packages
from setuptools import setup

setup(
    name='titan-rhv',
    version=0.11,
    description=(
        'A command line tool to talk with RHV environment'
    ),
    long_description=open('README').read(),
    author='Chen Chen',
    author_email='cchenlp@qq.com',
    maintainer='Chen Chen',
    maintainer_email='cchenlp@qq.com',
    license='BSD License',
    packages='titan',
    platforms=["all"],
    url='',
    #data_files=[("/usr/local/bin","src/titan")],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
    'ovirt-engine-sdk-python >= 4.2.9',
    'prettytable >= 0.7.2',
    ],
)
