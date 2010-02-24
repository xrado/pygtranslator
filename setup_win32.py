from distutils.core import setup
import py2exe
import glob
import sys
import os

opts = {
	'py2exe': {
		'includes': 'pango,atk,gobject,cairo,pangocairo,gtk.keysyms,encodings,encodings.*',
		'dll_excludes': [
			'iconv.dll','intl.dll','libatk-1.0-0.dll',
			'libgdk_pixbuf-2.0-0.dll','libgdk-win32-2.0-0.dll',
			'libglib-2.0-0.dll','libgmodule-2.0-0.dll',
			'libgobject-2.0-0.dll','libgthread-2.0-0.dll',
			'libgtk-win32-2.0-0.dll','libpango-1.0-0.dll',
			'libpangowin32-1.0-0.dll','libcairo-2.dll',
			'libpangocairo-1.0-0.dll','libpangoft2-1.0-0.dll',
		],
		'compressed':1,
		'optimize':2,
		'bundle_files':1
	}
}

setup(
	name = 'pyGtranslator',
	version = '0.5',
	description = 'GUI tool for google translator',
	author = 'xrado',
	url = 'http://xrado.hopto.org',
	license = 'GPL',

	windows = [{'script': 'pygtranslator','icon_resources':[(1,'pygtranslator.ico')]}],
	zipfile=None,
	options=opts,
	data_files=[
		('.', glob.glob('pygtranslator.glade')),
		('.', glob.glob('pygtranslator.ini')),
		('.', glob.glob('pygtranslator.png'))
	]
)
