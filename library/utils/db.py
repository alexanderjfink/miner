"""
DATABASE ABSTRACTIONS
"""

import mysql.connector as dbapi2
from mysql.connector import DatabaseError

from conf.settings import (VERBOSE, TMP_DIRECTORY, DELETE_TMP_ON_COMPLETE, 
							DICTIONARIES, DATABASES, DROP_IF_EXISTS)

class DBConnect: 
	# Function to connect to database
	# Abstract this eventually to make more DB options available
	def __init__(self):
		global DATABASES

		config = {
			'user': DATABASES['sql']['username'],
			'password': DATABASES['sql']['password'],
			'host': DATABASES['sql']['hostname'],
			'raise_on_warnings': False,
		}

		self.db = dbapi2.connect(**config)

		# Create cursor
		self.cursor = self.db.cursor()


	def create_db(self, db_name=None, query=None, drop_if_exists=False):
		"""
		Either want a database name or a full query to run through this abstracted method
		"""

		# can't do this without db_name
		if drop_if_exists and db_name:
			try:
				self.cursor.execute("DROP DATABASE %s;" % db_name)
			except DatabaseError:
				# We don't need to do anything with this, just need to try it.
				print "Error dropping current database."

		if query:
			try:
				self.cursor.execute(query)
			except DatabaseError:
				print "Error executing create database query."

			try:
				self.db.commit()
			except DatabaseError:
				print "Error committing creation of database."

			return True
		elif db_name:
			try:
				self.cursor.execute("CREATE DATABASE IF NOT EXISTS %s;" % db_name)
			except DatabaseError:
				print "Error executing create database based on database name."

			try:
				self.db.commit()
			except DatabaseError:
				print "Error committing creation of database."

			return True
		else:
			# fail if neither is specified
			return False


	def create_table(self, db_name=None, table_name=None, headers_types=None, query=None, drop_if_exists=False):
		"""
		Generate a create table query on a database
		"""
		if not db_name:
			db_name = self.db_name

		if drop_if_exists:
			try:
				self.cursor.execute("USE %s;" % db_name)
				self.cursor.execute("DROP TABLE IF EXISTS %s;" % table_name)
			except DatabaseError:
				print "Error dropping current table to create new one based on your specifications."
		
		if query:
			try:
				self.cursor.execute("USE %s;" % db_name)
				self.cursor.execute(query)
				self.db.commit()
			except DatabaseError:
				print "Error executing query to create database table."

			return True
		elif db_name and table_name and headers_types:
			try:
				self.cursor.execute("USE %s;" % db_name)
				self.cursor.execute("CREATE TABLE IF NOT EXISTS %s (%s);" % (table_name, headers_types))
				self.db.commit()
			except DatabaseError:
				print "Error executing generated query to create database table"

			return True
		else:
			# something didn't work
			print "Creation of table was NOT successful. Failing more or less gracefully..."
			return False

	def insert(self, db_name=None, table_name=None, values=None, query=None):

		if query:
			# if here, we've been sent a pre-prepared query
			try:
				self.cursor.execute(query)
				self.db.commit()
			except DatabaseError:
				print "Error inserting into database using query."

			return True
		elif db_name and table_name and values:
			try:
				self.cursor.execute("USE %s;" % db_name)
				self.cursor.execute("INSERT INTO %s VALUES (%s);" % (table_name, values))
				self.db.commit()
			except DatabaseError:
				print "Error inserting into database using generated query."
			return True
		else:
			# if here, we didn't get a query to run, so do what we need to...
			return False

	def query(self, db_name, query):
		if db_name and query:
			try:
				self.cursor.execute("USE %s;" % db_name)
				self.cursor.execute(query)
				self.db.commit()
			except DatabaseError:
				print "Your query() call didn't work as you expected. The databse did not accept it."
			return True
		else:
			# fail
			print "Query execution didn't go as expected."
			return False

	def commit(self):
		self.db.commit()

	def close(self):
		""" Call to close database """
		self.db.__del__()

	def __del__(self):
		""" Make sure not to leave the database hanging -- commit anything left over and close it down """
		self.db.commit()
		self.db.close()
