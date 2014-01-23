"""
HELPER FUNCTIONS
Contained within are functions that help along the major functionality of the software
They are within a separate file because they can be abstracted to use elsewhere

Eventually this file should be parsed out into separate helper functions for different modules.

Each of these functions has corresponding tests in tests/helpers_test.py
"""

import os, csv, sys, optparse
import messytables
import urllib2
import zipfile, tarfile
from messy2sql.core import Messy2SQL

from conf.settings import *

def download_file(url, map_name, file_rename, with_progress_bar=True, overwrite_if_exists=False):
	""" Download file and display progress bar """

	file_name = url.split('/')[-1]
	
	if not overwrite_if_exists and (os.path.exists((TMP_DIRECTORY + '%s' % (map_name + '/' + file_name)))):
		print "Your lucky day! You already have a local copy of this file..."
	else:
		u = urllib2.urlopen(url)
		f = open(file_name, 'wb')

		if with_progress_bar:
			meta = u.info()

			try:
				file_size = int(meta.getheaders("Content-Length")[0])
				print "Downloading: %s Bytes: %s" % (file_name, file_size)

				file_size_dl = 0
				block_sz = 8192
				while True:
					buffer = u.read(block_sz)
					if not buffer:
						break

					file_size_dl += len(buffer)
					f.write(buffer)
					status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
					status = status + chr(8)*(len(status)+1)
					print status,
			except IndexError: # Need this if file doesn't have content-length metadata
				print "File download complete."

		f.close()

		# need to rename the file to match the name in the Map
		root, ext = guess_extension(file_name)
		os.rename(file_name, file_rename + ext)


def get_filepaths(directory):
	"""
	This function will generate the file names in a directory 
	tree by walking the tree either top-down or bottom-up. For each 
	directory in the tree rooted at directory top (including top itself), 
	it yields a 3-tuple (dirpath, dirnames, filenames).

	Will avoid HIDDEN files

	From Johnny
	http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
	"""

	dir_paths = []
	file_paths = []  # List which will store all of the full filepaths.

	# Walk the tree.
	for root, directories, files in os.walk(directory):

		for filename in files:

			# Avoid hidden files
			if filename.startswith('.'): # fails on non *nix systems?

				# Join the two strings in order to form the full filepath.
				filepath = os.path.join(root, filename)

				file_paths.append(filepath)  # Add it to the list.

		for dirname in directories:

			dirpath = os.path.join(root, dirname)
			dir_paths.append(dirpath)

	return {'files': file_paths, 'directories': dir_paths}


def unpack_tar(filename):
	""" Take a filename, assume correct OS location """
	# open the tar file
	tfile = tarfile.open(filename)
	 
	if tarfile.is_tarfile(filename):
		# extract all contents
		tfile.extractall('.')

def unpack_gzip(filename):
	""" Take a filename, assume correct OS location """
	os.system("gzip -d " + filename)

def unpack_zip(filename):
	""" Take a zipfile, assume correct OS location """
	zipfile.extractall(filename)

def guess_extension(filename):
	"""
	Guess the extension of given filename.
	From: http://stackoverflow.com/a/9428460/1608991
	"""

	DOUBLE_EXTENSIONS = ['tar.gz','tar.bz2'] # Add extra extensions where desired.

	root,ext = os.path.splitext(filename)
	if any([filename.endswith(x) for x in DOUBLE_EXTENSIONS]):
		root, first_ext = os.path.splitext(root)
		ext = first_ext + ext
	return root, ext


def is_number(s):
	""" Test if string or # """
	try:
		float(s)
		return float(s)
	except ValueError:
		return s
		
# Functions to run bash from Python
# From Ian Bicking, http://stackoverflow.com/a/2654398/1608991
def run_script(script, stdin=None):
	""" Returns (stdout, stderr), raises error on non-zero return code """
	import subprocess
	# Note: by using a list here (['bash', ...]) you avoid quoting issues, as the
	# arguments are passed in exactly this order (spaces, quotes, and newlines won't
	# cause problems):
	proc = subprocess.Popen(['bash', '-c', script],
		stdout=subprocess.PIPE, stderr=subprocess.PIPE,
		stdin=subprocess.PIPE)
	stdout, stderr = proc.communicate()
	if proc.returncode:
		raise ScriptException(proc.returncode, stdout, stderr, script)
	return stdout, stderr

# Functions to run bash from Python
# From Ian Bicking, http://stackoverflow.com/a/2654398/1608991
class ScriptException(Exception):
	def __init__(self, returncode, stdout, stderr, script):
		self.returncode = returncode
		self.stdout = stdout
		self.stderr = stderr
		Exception.__init__('Error in script')