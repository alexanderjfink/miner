"""
Unit testing for Map.py
"""

from library.miner.map import Map
import nose

class TestSQLMap():
	"""
	Unittest to try making a Map that is a SQL map.
	Test needs to setup with a .csv style dataset.
	"""
	def setUp(self):
		""" Create a fake dataset to use to insert """

		pass

	def is_installed_test(self):
		""" Should pass if this is already installed in standard area """
		pass

	def test_setup(self):
		""" Should pass if directory is created in TEMP and if OS is pointed to that directory """


	def test_download(self):
		""" Should pass if download completes and dataset resides in tmp/ """
		pass

	def test_unpack(self):
		""" Should pass if files exist on disk """
		pass

	def test_install(self):
		""" Should pass if data gets inserted into SQL database """
		pass

	def test_cleanup(self):
		""" Should pass if data created in download & unpack is deleted """
		pass

	def tearDown(self):
		""" Destroy fake dataset and database changes (if any) """
		pass

class TestDocstoreMap():
	pass

class TestKeyValueMap():
	pass



