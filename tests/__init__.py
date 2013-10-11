"""
Setup universal package tests with nose
"""

import nose

csv_test_file = ""
sql_test_file = ""

def setUpPackage():
	"""
	Setup for testing w/fake database
	"""
	csv_test_file = "id,name,email,date,info1,info2,info3\n3,josephine,jojo@web.com,10/10/2013,interesting things, more interesting 'things' about me,others"

def tearDownPackage():
	"""
	Tear down fake database
	"""
	pass


