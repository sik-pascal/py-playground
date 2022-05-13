from random import betavariate
from setuptools import find_packages, setup

with open('README.md', 'r') as rm:
    long_desc = rm.read()

setup(
    name='pgbackup',
    version='1',
    author='Slava',
    description='Python CLI tool for db backup',
    long_description=long_desc,
    packages= find_packages('src')
)
