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

	# These are here rather than in __init__ so that subclasses can simply define each of these
	# within the subclass maps
	
	# URL for homepage of dataset (e.g. http://census.gov/)
	homepage = ''

	description = ''

	# Specific URLs for the dataset downloads
	# needs to be a dictionary ala
	# data = {'census1': {url: 'http://www.census.gov/census1.zip', mirror: '', sha1: '', dictionary: ''}}
	data = {}

	# type of database to install e.g. 'docstore','sql','keyvalue'
	# see conf/settings.py for available databases
	db_type = 'sql'

	db_name = ''


	def __init__(self, mirrors=None, sha1=None, dictionary=None, db_name=None):

		# Mirror in case this dataset goes down
		if mirror:
			self.mirror = mirror

		# sha1 checksum for dataset download
		if sha1:
			self.sha1 = sha1

		# URLs for the data dictionaries
		if dictionary:
			self.dictionary = dictionary

		# specific database name specified
		if db_name:
			self.db_name = db_name


	def __is_installed(self):
		"""
		Utility to check if Map is already installed in base database using available
		databases and db prefix names
		"""

		# open MySQL connection
		db = DBConnect()

		# Create cursor
		cursor = db.cursor()

		# Create database if it isn't there already
		return cursor.execute(("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '%s';" % self.db_name))
		

	def setup(self):
		""" Need to prep by creating a folder and changing the system into that directory """
		
		if global VERBOSE:
			print "Initializing temporary working directory..."

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
		for url in data:
			download_file(url.url, with_progress_bar=True)

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
			'xls': pass,
			'xlsx': pass,
			'html': pass,
			'pdf': pass,
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

			# separate out the file extension
			root, ext = guess_extension(file_name)

			# using file type, extract this file!
			file_types[ext](os.path.basename(f))



	def install(self):
		"""
		Does installation of the files into user's chosen database

		NOTES:
			- Does installation have to assume that it can just install from each of the files available? Do we
			  have to re-write the installer for something complex like the US Census? And is that an acceptable level
			  of configuration for a Map?
		"""

		# for every file
		files = os.listdir('./')

		for f in files:
			file_name = os.path.basename(f)
			root, ext = guess_extension(file_name)
			
			if ext == "sql":
				# if we have a SQL file, we should run that
				db.create_table()
				db.insert()

			elif ext in ("csv", "pdf", "xlsx", "html"):	
				# create messy2sql instance
				m2s = Messy2SQL(file_name, DATABASES['sql'].TYPE)
				# if we have PDF, HTML, CSV, or Excel files, we should use messy2sql
				# get a table query, run it!
				
				# use messytables to build a MessyTables CSV
				rows = CSVTableSet(file_name).tables[0]

				# use the rowset here to create a sql table query and execute
				db.create_table(query = m2s.create_sql_table(rows))

				# get insert statements
				db.insert(query = m2s.create_sql_insert(rows))

				# and finally, commit
				db.commit()
			else:
				pass

	def cleanup(self):

		if global VERBOSE:
			print "Cleaning up folders and closing DB connections..."
		
		# need to delete all the files in tmp/thismap
		os.chdir('../')
		os.rmdir(self.__name__)

		# close DB connection
		cursor.close()
		cnx.close()
	