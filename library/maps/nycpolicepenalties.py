""" 
miner map for NYC Police Department Penalties data
Data is released publicly by the City of New York
"""

from library.miner.map import Map

class NYCPolicePenalties(Map):
	description = 'Penalties for police in NYC'
	homepage = 'http://data.cityofnewyork.us'

	data = {
		'nyc_police_penalties': {
			'url': "https://data.cityofnewyork.us/api/views/ns22-2dcm/rows.csv",
			'mirror': "",
			'sha1': "",
			'dictionary': "",
		},
	}
	
	db_type = 'sql'