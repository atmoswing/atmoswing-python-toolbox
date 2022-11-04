# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='atmoswing-toolbox',
    version='0.1.0',
    description='Package for AtmoSwing',
    long_description=readme,
    author='Pascal Horton',
    author_email='pascal.horton@giub.unibe.ch',
    url='https://github.com/atmoswing/tools-py',
    license=license,
    packages=find_packages(exclude=('tests', 'examples'))
)
