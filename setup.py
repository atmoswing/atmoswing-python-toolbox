from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='atmoswing-toolbox',
    version='0.1.0',
    description='Python tools for AtmoSwing',
    long_description=readme,
    author='Pascal Horton',
    author_email='pascal.horton@giub.unibe.ch',
    url='https://github.com/atmoswing/atmoswing-python-toolbox',
    license=license,
    packages=find_packages(exclude=('tests', 'examples'))
)
