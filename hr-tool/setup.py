from setuptools import setup, find_packages

setup(
    name='hr',
    version='1',
    author='Slava',
    description='Python CLI tool to help HR',
    long_description='Export user info as json or csv ',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'hr=hr.cli:main'
        ],
    }
)
