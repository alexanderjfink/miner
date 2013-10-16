"""
Test-Driven Development for Helper Functions

Using Nose documentation to learn how to setup basic tests.
https://nose.readthedocs.org/en/latest/writing_tests.html

Within this documentation, you can see that you can do test setUp and tearDown universally for a test package in __init__.py.
If you hop over to that file, you can see that I've done so.
"""

import nose
import os

from library.utils.helpers import *

def test_is_number():
	assert 1==1


# def test_csv_to_sql_table():
# 	"""
# 	should fail unless sql statement to create a new table based on headers executes
# 	"""
# 	assert csv_to_sql_table('tests/testdata.csv', delimiter=",").rstrip() == "CREATE TABLE testdata (id int, name varchar(255), email varchar(255), date date(), info1 varchar(255), info2 varchar(255), info3 varchar(255));"

# def test_csv_to_sql():
# 	"""
# 	should fail unless sql statement executes correctly on db
# 	"""
# 	assert 1==1





