from setuptools import find_packages, setup

with open('README.md', 'r') as rm:
    long_desc = rm.read()

setup(
    name='pgbackup',
    version='1',
    author='Slava',
    description='Python CLI tool for db backup',
    long_description=long_desc,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['boto3'],
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main'

        ],
    }
)
