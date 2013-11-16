"""
miner map for US Non-Profit Form 990 data
Data is released publicly by CitizenAudit

This should demonstrate exactly how simple a Map can be...
"""

from library.miner.map import Map

class USForm990Extracts(Map):
	homepage = 'http://www.citizenaudit.org'
	description = 'US Non-Profit Form 990 Tax information released by CitizenAudit'

	data = {
		'extracts': {
			'url': "http://s3.citizenaudit.org/irs/bulk/manifest.csv.gz",
			'mirror': "",
			'sha1': "",
			'dictionary': "",
		},
		'2012': {
			'url': "http://s3.citizenaudit.org/irs/bulk/manifest.csv.gz",
			'mirror': "",
			'sha1': "",
			'dictionary': "",
		}

	}
	
	db_type = 'sql'
	