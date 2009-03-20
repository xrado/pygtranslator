#!/usr/bin/env python

from distutils.core import setup, Extension

setup(name='pyGtranslator',
	version='0.2',
	description='GUI tool for Google translate',
	author='Radovan Lozej',
	author_email='radovan(dot)lozej(at)gmail(dot)com',
	url='http://xrado.hopto.org',
	classifiers=[
		'Environment :: X11 Applications',
		'Intended Audience :: End Users/Desktop',
		'License :: GNU General Public License (GPL)',
		'Operating System :: Linux',
		'Programming Language :: Python',
		'Topic :: Accessories'
		],
	scripts = ['pygtranslator'],
	data_files=[
		("doc/pygtranslator-0.1", ["README"]),
		("share/pygtranslator", ["pygtranslator.glade"]),
		('share/applications', ['pygtranslator.desktop']),
		('share/pixmaps', ['pygtranslator.png'])
	]
)
