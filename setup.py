#! /usr/bin/env python
# -*- coding: utf8 -*-


try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
 
config = {
	'name': 'BioLoader',
	'description': 'Collection of tools for ftp data, synchronization',
	'author': 'Abhishek Tiwari',
	'url': 'http://github.com/abhishektiwari/BioLoader',
	'download_url': 'http://github.com/abhishektiwari/BioLoader',
	'author_email': 'abhishek@abhishek-tiwari.com',
	'version': '0.1',
	'install_requires': ['tweepy','ftputil'],
	'packages': ['bioloader', 'bioftp', 'bioftpalerts'],
	'scripts': [],
}

setup(**config)
