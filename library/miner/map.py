"""
The basic form of a Map...
Should be general enough that it can fit all maps (unless there seems good reason to ignore this)
Should be specific enough that it does a lot of the heavy lifting for Maps
"""

# Python standard
import re, os, shutil

# External libraries
from messy2sql.core import Messy2SQL
from messytables import CSVTableSet, HTMLTableSet, XLSTableSet, PDFTableSet

# Local to project
from conf.settings import *
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
	# TODO: data is downloaded and added to databases in the order listed here. if one set depends on installation of another, put the
	# dependent ones later
	data = {}

	# type of database to install e.g. 'docstore','sql','keyvalue'
	# see conf/settings.py for available databases
	db_type = 'sql'

	db_name = ''


	def __init__(self, db_name=None):

		# specific database name specified
		if db_name:
			self.db_name = db_name

					# open MySQL connection
		self.db = DBConnect()


	def __is_installed(self, db_name):
		"""
		Utility to check if Map is already installed in base database using available
		databases and db prefix names
		"""

		# Create database if it isn't there already
		# Need to check that this returns TRUE
		return self.db.query(("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '%s';" % self.db_name))

	def setup(self):
		""" Need to prep by creating a folder and changing the system into that directory """

		if VERBOSE:
			print "Initializing temporary working directory..."

		# make directory for this in temp dir + name_of_map
		# switch to this directory
		os.chdir(TMP_DIRECTORY)

		try:
			os.mkdir(self.__class__.__name__)
		except OSError:
			print "Directory already exists for this file..."

		os.chdir((TMP_DIRECTORY + '%s' % self.__class__.__name__))		

	def download(self):
		"""
		Using data dictionary of urls, grab the files and display a nice progress bar while doing it
		"""
		
		if VERBOSE:
			print "Downloading data files..."

		os.chdir(TMP_DIRECTORY + "%s" % self.__class__.__name__)

		# need an iterator to download what is either a single page or a load of files, but that should get specified.
		# this should be the easiest one to write
		for k, v in self.data.iteritems():
			## TODO: FIX THIS TO WORK WITH NEW WAY OF ORGANIZING FILES
			download_file(url=v['url'], map_name=self.__class__.__name__, file_rename=k, with_progress_bar=True)

	def unpack(self):
		"""
		Unpack the downloads into the root directory for this map
		"""

		if VERBOSE:
			print "Unpacking data files to disk..."

		# need to check what file type we've got now...
		file_types = {
			'.csv': lambda x: None, # Don't need to unpack these types of files
			'.sql': lambda x: None,
			'.xls': lambda x: None,
			'.xlsx': lambda x: None,
			'.html': lambda x: None,
			'.pdf': lambda x: None,
			'.tar': unpack_tar,
			'.tgz': unpack_tar,
			'.tar.gz': unpack_tar,
			'.gz': unpack_gzip,
			'.zip': unpack_zip,
		}

		# get all files in working directory of this map
		files = os.listdir(TMP_DIRECTORY + '%s/' % self.__class__.__name__)

		# iterate through files
		for f in files:
			# get file name to unpack
			file_name = os.path.basename(f)

			# separate out the file extension
			root, ext = guess_extension(file_name)

			# create new directory for file
			os.mkdir(root)

			# move file into directory
			os.rename('./' + file_name, './' + root + '/' + file_name)

			# switch to directory
			os.chdir(root)

			# using file type, extract this file!
			file_types[ext](file_name)

			# switch back
			os.chdir('../')

		print "Unpacking complete..."


	def install(self, drop_if_exists=False):
		"""
		Does installation of the files into user's chosen database

		This is a primarily internal method, but if base it should just get called.

		NOTES:
			- Does installation have to assume that it can just install from each of the files available? Do we
			  have to re-write the installer for something complex like the US Census? And is that an acceptable level
			  of configuration for a Map? (One potential answer - can do some pre-work on the data in the Map, then call this default function to finish job)

		TODO:
			- Need to fix how headers work -- can specify whether headers are present, whether all data should be installed
			  into the same database?
		"""

		if VERBOSE:
			print "Beginning copy of data to local disk."

		# check if we need a separate db for each url or whether one is enough
		# one is enough if specified here
		if self.db_name:
			db_name = self.db_name
			self.db.create_db(self.__class__.__name__)


		# X - TODO: ITERATE OVER EACH SUBFOLDER (we know that the folders have the name of the file? there should be same number of folders as there are urls being extracted...)
		# X - MAKE A DB FOR EACH SUBFOLDER W/PREFIXES (BOTH DEFAULT IN SETTINGS AND FOR THIS DATASET)
		# X - ITERATE OVER EACH FILE IN SUBFOLDER
		# X - MAKE A TABLE FOR EACH FILE
		# X - INSERT DATA INTO TABLE

		# for every file url
		# for k, v in self.data.iteritems():

		# Build a set of folders
		for dirs in get_filepaths(os.getcwd())['directories']: # assume we are in right directory is probably bad choice UNSAFE
			# now we have a list of the directories within this directory

			os.chdir(dirs) # change to directory here UNSAFE


			## Perform operations at directory level - create database w/name of directory as name

			path_name = os.path.basename(dirs) # dir path name
			# root, ext = guess_extension(self.data[path_name]['url'])
			# file_name = os.path.basename(root + ext) # PROBLEM IS WITH GUESSED NAME OF FILE HERE>... may make more than one file, not by same name...

			# If we don't have a db name, we should find it in the URLs
			if self.db_name:
				db_name = self.db_name
			elif 'database' in v: # check if database name is specified in map
				db_name = self.data[path_name]['database']
			else: # at this point, we just need to give it a name... so name it the maps name
				db_name = path_name
			
			self.db.create_db(db_name=db_name) # Should only create if not already there...
			

			# Iterate through each file in directory, create a table, insert data
			for files in get_filepaths(os.getcwd())['files']:
				
				if ext == ".sql":
					# if we have a SQL file, we should run that
					# TODO: THIS DOESN'T ACTUALLY WORK, BUT WE NEED TO DO SOMETHING LIKE THIS
					self.db.query(f)

				elif ext in (".csv", ".pdf", ".xls", ".xlsx", ".html"):	
					# create messy2sql instance
					m2s = Messy2SQL(file_name, DATABASES['sql']['type'], table_name=k)
					# if we have PDF, HTML, CSV, or Excel files, we should use messy2sql
					
					# get a table query, run it!
					try:
						fh = open((TMP_DIRECTORY + self.__class__.__name__ + '/' + file_name), 'rb')
					except IOError:
						print "Opening file failed or file does not exist."
					
					print fh.read()

					# use messytables to build a MessyTables RowSet with file type
					rows = {
						'.csv': CSVTableSet(fh).tables[0],
						#'.pdf': PDFTableSet(file_name),
						#'.xlsx': XLSTableSet(file_name),
						#'.xls': XLSTableSet(file_name),
						#'.html': HTMLTableSet(file_name),
					}[ext]

					for row in rows:
						print "Hello"
					# use the rowset here to create a sql table query and execute
					self.db.create_table(query = m2s.create_sql_table(rows), db_name=db_name, drop_if_exists=drop_if_exists)

					# get insert statements
					query = m2s.create_sql_insert(rows)
					print query
					self.db.insert(query = query, db_name=db_name, table_name=k)
				else:
					print "File type did not match supported types..."


	def cleanup(self):
		global VERBOSE

		if VERBOSE:
			print "Cleaning up folders and closing DB connections..."
		
		# need to delete all the files in tmp/thismap
		os.chdir('../')
		shutil.rmtree(self.__class__.__name__)

		# close DB connection
		self.db.close()
	