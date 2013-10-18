"""
miner map for Medicare Official Hospital Compare data
Data is released publicly by data.Medicare.gov
"""

class MedicareHospitalCompare(miner.Map):
	description = 'Medicare Official Hospital Compare data released by Medicare'
	homepage = 'https://data.medicare.gov/data/hospital-compare'

	data = {
		'extracts': {
			'url': "https://data.medicare.gov/views/bg9k-emty/files/_iaeWFLeLd_bvpAxvmS4zCbU0ytLTKBH1gL9RwRo2A4?filename=Hospital_Compare.zip&content_type=application%2Fzip%3B%20charset%3Dbinary",
			'mirror': "",
			'sha1': "",
			'dictionary': "",
		}
	}
	
	db_type = 'sql'
	