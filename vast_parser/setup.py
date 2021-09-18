from setuptools import find_packages, setup

setup(
    name='vast_parser',
    packages=find_packages(include=['vast_parser']),
    version='0.1.0',
    description='VAST XML Parser',
    author='Tim Pavlov',
    install_requires=['dexml==0.5.1'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)