import os

from configparser import ConfigParser, ExtendedInterpolation

from setuptools import find_packages, setup

EXCLUDE_FROM_PACKAGES = [
    'tests*',
]

INSTALL_REQUIRES = [
    'setuptools',
    'pip',
    'boto3'
]

SETUP_DIR = os.path.abspath(os.path.dirname(__file__))
config = ConfigParser(interpolation=ExtendedInterpolation(), empty_lines_in_values=False)
config.read(os.path.join(SETUP_DIR, 'metadata.ini'))

setup(
    name=config.get('META', 'name'),
    description=config.get('META', 'description'),
    long_description=config.get('META', 'long_description'),
    license=config.get('META', 'license'),
    author=config.get('META', 'author'),
    author_email=config.get('META', 'author_email'),
    url=config.get('META', 'url'),
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=False,
    install_requires=INSTALL_REQUIRES,
    zip_safe=False,
    test_suite="tests"
)
