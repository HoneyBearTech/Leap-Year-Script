"""A setup module for LeapYearScript."""

import base64
import re

from setuptools import setup


def get_long_description():
    """Transform README.md into a usable long description.

    Replaces relative references to svg images to absolute https references.
    """

    with open('README.md') as f:
        read_me = f.read()

    def replace_relative_with_absolute(match):
        svg_path = match.group(0)[1:-1]
        return ('(https://github.com/HoneyBearTech/LeapYearScript'
                '%s?sanitize=true)' % svg_path)

    return re.sub(r'\(tests/golden-images/.*?\.svg\)',
                  replace_relative_with_absolute, read_me)


setup(
    name='LeapYearScript',
    version='1.0.0',  # Also change in version.py.
    author='HoneyBearTech',
    author_email='sstoube@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    description='Simple python script to determine leap years',
    keywords="github gh-badges badge shield status",
    package_data={
        'LeapYearScript': [
            'badge-template-full.svg', 'default-widths.json', 'py.typed'
        ]
    },
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    python_requires='>=3.4',
    install_requires=['Jinja2>=3,<4', 'requests>=2.22.0,<3'],
    extras_require={
        'pil-measurement': ['Pillow>=6,<10'],
        'dev': [
            'Flask>=2.0',  # For server tests. 
            'fonttools>=3.26',
            'nox',
            'Pillow>=5',
            'pytest>=3.6',
            'xmldiff>=2.4'
        ],
    },
    license='Apache-2.0',
    packages=["LeapYearScript"],
    url='https://github.com/HoneyBearTech/LeapYearScript')
