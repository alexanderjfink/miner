# sql_database						connection information for relational database
# nosql_database					connection information for doc store
# tmp_directory						directory to store temporary download files while extracting
# delete_tmp_on_extract_complete	delete or save temporary files when extracting is finished?
# drop_if_exists					if database or table already exists, should it be ignored or dropped?
# debug								should debug information be displayed?

conf = {
	'sql_database': {
		'type': 'mysql',
		'username': 'specialuser',
		'password': 'specialpass',
		'hostname': 'localhost',
		'database_prefix': 'miner_',
	},

	'nosql_database': {
		'type': 'hadoop',
	},

	'tmp_directory': './tmp/',
	'delete_tmp_on_extract_complete': True,
	'drop_if_exists': True,
	'debug': True,
}