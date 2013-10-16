"""
Global Settings

settings.py initiates global settings. Keeps all of these in one area so users can easily update and change based
on their own needs.

Global settings need to be imported into functions and classes with the 'global' keyword before the variable/function name
They are all in capital letters to differentiate them from other variables which are in lower case and separated by underscores '_'

Eventually setup.py should allow the user to configure these on first use or installation of the software so that they work
However, at this point, the user will need to update these themself.
"""

#################
# CORE SETTINGS #
#################

# debug								should debug information be displayed?
DEBUG = True

# TMP_DIRECTORY						directory to store temporary download files while extracting
TMP_DIRECTORY = "./tmp"

# DELETE_TMP_ON_COMPLETE			delete or save temporary files when extracting is finished?
DELETE_TMP_ON_COMPLETE = True


#####################
# DATABASE SETTINGS #
#####################

# SQL_DATABASE						connection information for relational database
# NOSQL_DATABASE					connection information for docstore database

# At minimum, SQL_DATABASE and NOSQL_DATABASE must be installed
# Different maps will prefer certain database types, not all types are appropriate for each map

DATABASES = {
		'sql': {
			'TYPE': 'mysql',
			'USERNAME': 'specialuser',
			'PASSWORD': 'specialpass',
			'HOSTNAME': 'localhost',
			'DB_PREFIX': 'miner_', # If DB_PREFIX isn't set, no prefix will be used
		},

		'docstore': {
			'TYPE': 'hadoop',
		},

		'keyvalue': {
			'TYPE': 'redis',
		}
	}

# DROP_IF_EXISTS					if database or table already exists, should it be ignored or dropped?
DROP_IF_EXISTS = True