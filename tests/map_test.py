"""
Unit testing for Map.py
"""
import unittest
import nose

import os
import shutil
from library.miner.map import Map
from library.utils.db import DBConnect
from conf.settings import *

class TestSQLMap(unittest.TestCase):
	"""
	Unittest to try making a Map that is a SQL map.
	Test needs to setup with a .csv style dataset.
	"""
	def setUp(self):
		""" Create a fake dataset to use to insert """

		global PROJECT_ROOT

		self.db = DBConnect()
		self.db.create_db("test_db")

		self.test_map = Map(db_name="test_db")

		self.test_map.homepage = "http://www.mytestingdata.com/"
		self.test_map.description = "The testing data for my Maps"
		self.test_map.data = {
								'testdata': {
									'url': ("file:///" + PROJECT_ROOT + "tests/testdata.csv"),
									'mirror': "",
									'sha1': "",
									'dictionary': "",
								},
								'testdata2': {
									'url': ("file:///" + PROJECT_ROOT + "tests/testdata.csv"),
								},

								## TODO: ADD ANOTHER TEST FILE HERE THAT IS COMPRESSED
							}
		self.test_map.db_type = 'sql'
		self.test_map.db_name = 'test_db'
		self.test_map.__name__ = "Map"


	def is_installed_test(self):
		""" Should pass if this is already installed in standard area """
		pass

	def test_setup(self):
		""" Should pass if directory is created in TEMP and if OS is pointed to that directory """
		self.test_map.setup()

		try:
			os.chdir(TMP_DIRECTORY + 'Map')
		except OSError:
			assert 0 == 1 # now we know this failed in the tests
			print "Could not find test data directory"

	def test_download(self):
		""" Should pass if download completes and dataset resides in tmp/ """
		self.test_map.download()

		self.assertEqual(os.path.exists(TMP_DIRECTORY + "Map/testdata.csv"), True)

	def test_unpack(self):
		""" Should pass if files exist on disk """
		self.test_map.unpack()

		self.assertEqual(os.path.exists(TMP_DIRECTORY + "Map/testdata/testdata.csv"), True)

	def test_install(self):
		""" Should pass if data gets inserted into SQL database """
		self.test_map.install(drop_if_exists=True)

		# self.db.query("SELECT * FROM ")

	def test_cleanup(self):
		""" Should pass if data created in download & unpack is deleted """
		pass

	def tearDown(self):
		""" Destroy fake dataset and database changes (if any) """
		pass
		# shutil.rmtree(TMP_DIRECTORY + "TestMap")

class TestDocstoreMap():
	pass

class TestKeyValueMap():
	pass



