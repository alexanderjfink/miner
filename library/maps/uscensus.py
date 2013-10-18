"""
miner map for US Census 2010 data
Data is released publicly by census.gov
"""

class USCensus2010(miner.Map):
	description = 'Data from the 2010 Dicennial US Census.'
	homepage = 'http://www.census.gov'

	data = {
		'uscensus': {		# general table format from SQL
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/SF1_Access2003.mdb",
			'mirror': "",
			'sha1': "",
			'dictionary': "",
		},
		'ca': {
			'url': "",
			'mirror': "",
			'sha1': "",
			'dictionary': "",
		},
		'mi': {
			'url': "",
			'mirror': "",
			'sha1': "",
			'dictionary': "",
		},
		'mn': {
			'url': "http://s3.citizenaudit.org/irs/bulk/manifest.csv.gz",
			'mirror': "",
			'sha1': "",
			'dictionary': "",
		},
		'ny': {
			'url': "",
			'mirror': "",
			'sha1': "",
			'dictionary': "",
		},
		'wi': {
			'url': "",
			'mirror': "",
			'sha1': "",
			'dictionary': "",
		},
	}
	
	db_type = 'sql'
	