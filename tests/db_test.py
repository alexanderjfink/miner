""" Testing for DB """

import unittest
import nose

from library.utils.db import *

import mysql.connector as dbapi2

class DBTest(unittest.TestCase):
	def setUp(self):
		self.db = DBConnect()

		# WE also need to create our own connection to the database for testing purposes
		global DATABASES

		config = {
			'user': DATABASES['sql']['username'],
			'password': DATABASES['sql']['password'],
			'host': DATABASES['sql']['hostname'],
			'raise_on_warnings': False,
		}

		self.db_test = dbapi2.connect(**config)
	    
		# Create cursor
		self.cursor = self.db_test.cursor()

	# def tearDown(self):
	# 	try:
	# 		self.cursor.execute("DROP DATABASE test_db;")
	# 	except DatabaseError:
	# 		pass
	# 	self.db.commit()
	# 	self.db.close()


	def test_create_db(self):
		""" Should fail unless a database can be found created in the connected to server """

		self.assertEqual(self.db.create_db("test_db", drop_if_exists=True), True) # check that this returns true

		try:
			self.cursor.execute("USE test_db;")
		except DatabaseError:
			assert 0 == 1 # we failed, let us know via the test
			print "Creating database failed."


	def test_create_table(self):
		""" Should pass if test table is successfully created and can be selected from without error """
		
		self.assertEqual(self.db.create_table(db_name="test_db", table_name="test_table", 
												headers_types="id INT, test1 VARCHAR(255), test2 VARCHAR(128), dt DATETIME"), True)

		try:
			self.cursor.execute("USE test_db;")
			self.cursor.execute("SELECT * FROM test_table;")
		except DatabaseError:
			assert 0 == 1 # we failed, let us know via the test
			print "Creating table failed."


	def test_insert(self):
		""" Should fail unless the insert into database works! """
		
		self.assertEqual(self.db.insert(db_name="test_db", table_name="test_table", values="1,'pete seeger','myles horton', 2013-10-10"), True)

		try:
			self.cursor.execute("USE test_db;")
			self.cursor.execute("SELECT * FROM test_table WHERE id=1;")
		except DatabaseError:
			assert 0 == 1 # we failed, let us know via the test
			print "Inserting into table failed."

	def test_query(self):
		"""
		Should fail unless sql statement executed works...
		"""
		
		self.assertEqual(self.db.query("test_db", "INSERT INTO test_table VALUES (2, 'dr. king', 'huey newton', 2013-10-10;"), True)
		try:
			self.cursor.execute("USE test_db;")
			self.cursor.execute("SELECT * FROM test_table WHERE id=2;")
		except DatabaseError:
			assert 0 == 1 # we failed, let us know via the test
			print "Inserting into table failed."