"""
The basic form of a Map...
Should be general enough that it can fit all maps (unless there seems good reason to ignore this)
Should be specific enough that it does a lot of the heavy lifting for Maps
"""

import messy2sql
import re, os
from library.utils.helpers import download_file, unpack_tar, unpack_gzip, unpack_zip, guess_extension
from library.utils.db import DBConnect


class Map:
	# Methods internal to Maps class

	def __init__(self, homepage, urls, db_type, mirror=None, sha1=None, dictionary=None, db_name=None):
		# URL for homepage of dataset (e.g. http://census.gov/)
		self.homepage = homepage

		# Specific URLs for the dataset downloads
		# needs to be a dictionary ala
		# urls = {'census1': 'http://www.census.gov/census1.zip', 'census2':'http://www.census.gov/census2.zip'}
		self.url = urls


		# type of database to install e.g. 'docstore','sql','keyvalue'
		# see conf/settings.py for available databases
		self.db_type = db_type

		# Mirror in case this dataset goes down
		if mirror:
			self.mirror = mirror
		else:
			self.mirror = []

		# sha1 checksum for dataset download
		if sha1:
			self.sha1 = sha1
		else:
			self.sha1 = []

		# URLs for the data dictionaries
		if dictionary:
			self.dictionary = dictionary
		else:
			self.dictionary = []

		if db_name:
			self.db_name = db_name
		else:
			self.db_name = self.__name__


	def __is_installed(self):
		"""
		Utility to check if Map is already installed in base database using available
		databases and db prefix names
		"""

		# open MySQL connection
		db = DBConnect()
		cnx = db.connect()

		# Create cursor
		cursor = cnx.cursor()

		# Create database if it isn't there already
		return cursor.execute(("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '%s';" % self.db_name))
		

	def setup(self):
		""" Need to prep by creating a folder and changing the system into that directory """

		# make directory for this in temp dir + name_of_map
		# switch to this directory
		os.chdir('./tmp')

		try:
			os.mkdir(self.__name__)
		except OSError:
			print "Directory already exists for this file..."

		os.chdir('./tmp/%s')  % self.__name__

		# in case of sql, create a database here
		# commit query

	def download(self):
		"""
		Using data dictionary of urls, grab the files and display a nice progress bar while doing it
		"""

		if global VERBOSE:
			print "Downloading data files..."

		# need an iterator to download what is either a single page or a load of files, but that should get specified.
		# this should be the easiest one to write
		for url in urls:
			download_file(url, with_progress_bar=True)

		# use a messy2sql because we'll need it
		# eventually this can be part of an IF import -- we only need it if we are doing SQL
		#m2s = Messy2SQL()
		

	def unpack(self):
		"""
		Unpack the downloads into the root directory for this map
		"""

		if global VERBOSE:
			print "Unpacking data files to disk..."

		# need to check what file type we've got now...
		file_types = {
			'csv': pass,
			'sql': pass,
			'tar': unpack_tar,
			'gz': unpack_gzip,
			'tgz': unpack_tar,
			'tar.gz': unpack_tar,
			'zip': unpack_zip,
		}

		# get all files in working directory of this map
		files = os.listdir('./')

		# iterate through files
		for f in files:
			file_name = os.path.basename(f)

			# using file type, extract this file!
			file_types[guess_extension(file_name)](os.path.basename(f))




	def install(self):
		# base install for a sql file should be to just read each file in directory with messytables and then insert it into table

		# get a table query, run it!
		m2s.create_sql_table(rows)

		# run & commit query

		# get insert statements
		m2s.create_sql_insert(rows)

		# run & commit query

	def cleanup(self):

		if global VERBOSE:
			print "Cleaning up folders and closing DB connections..."
		
		# need to delete all the files in tmp/thismap
		os.chdir('../')
		os.rmdir(self.__name__)

		# close DB connection
		cursor.close()
		cnx.close()
	