# -*- coding: utf-8 -*-
# @Author: broono
# @Date:   2016-06-31
# @Email: tosven.broono@gmail.com


import codecs
import os

try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


NAME = "freexici"
PACKAGES = find_packages()
REQUIREMENTS = ["requests", "bs4", "selenium"]
DESCRIPTION = "A simple tool to scrape & generate random & usable web proxies."
LONG_DESCRIPTION = read("README.rst")
KEYWORDS = "proxy proxies xicidaili freexici"
AUTHOR = "Broono"
AUTHOR_EMAIL = "tosven.broono@gmail.com"
URL = "https://github.com/brunobell/freexici"
VERSION = "0.0.1"
LICENSE = "MIT"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    platforms=['any'],
    include_package_data=True,
    zip_safe=True,
    install_requires=REQUIREMENTS,
)
