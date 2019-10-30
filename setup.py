"""Package configuration for Dwolla."""
import os

from setuptools import find_packages, setup


def read(filename):
    """Read file contents."""
    path = os.path.realpath(os.path.join(os.path.dirname(__file__), filename))
    with open(path, 'rb') as f:
        return f.read().decode('utf-8')


dependencies = read('requirements.txt').split()
setup(
    name='dwolla',
    version='1.0.1',
    description='A Python package for a technical interview problem',
    url='https://github.com/NickolasHKraus/dwolla',
    author='Nickolas Kraus <NickHKraus@gmail.com>',
    install_requires=dependencies,
    packages=find_packages(exclude=['*.test', '*.test.*', 'test.*', 'test']),
    entry_points={
        'console_scripts': ['dwolla=dwolla.cli:cli'],
    },
    include_package_data=True,
    zip_safe=False)
