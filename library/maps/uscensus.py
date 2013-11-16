"""
miner map for US Census 2010 data
Data is released publicly by census.gov
"""

from library.miner.map import Map

class USCensus2010(Map):
	description = 'Data from the 2010 Dicennial US Census.'
	homepage = 'http://www.census.gov'

	data = {
		'uscensus': {		# general table format from SQL
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/SF1_Access2003.mdb",
			'mirror': "",
			'sha1': "",
			'dictionary': "",
		},
		'al': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Alabama/al2010.sf1.zip",
		},
		'ak': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Alaska/ak2010.sf1.zip",
		},
		'az': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Arizona/az2010.sf1.zip",
		},
		'ar': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Arkansas/ar2010.sf1.zip", 
		},
		'ca': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/California/ca2010.sf1.zip",
			'mirror': "",
			'sha1': "",
			'dictionary': "",
		},
		'co': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Colorado/co2010.sf1.zip",
		},
		'ct': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Connecticut/ct2010.sf1.zip",
		},
		'de': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Delaware/de2010.sf1.zip",
		},
		'dc': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/District_of_Columbia/dc2010.sf1.zip",
		},
		'fl': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Florida/fl2010.sf1.zip",
		},
		'ga': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Georgia/ga2010.sf1.zip",
		},
		'hi': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Hawaii/hi2010.sf1.zip",
		},
		'id': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Idaho/id2010.sf1.zip",
		},
		'il': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Illinois/il2010.sf1.zip",
		},
		'in': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Indiana/in2010.sf1.zip",
		},
		'ia': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Iowa/ia2010.sf1.zip",
		},
		'ks': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Kansas/ks2010.sf1.zip"
		},
		'ky': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Kentucky/ky2010.sf1.zip",
		},
		'la': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Louisiana/la2010.sf1.zip",
		},
		'me': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Maine/me2010.sf1.zip",
		},
		'md': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Maryland/md2010.sf1.zip",
		},
		'ma': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Massachusetts/ma2010.sf1.zip",
		},
		'mi': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Michigan/mi2010.sf1.zip",
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
		'ms': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Mississippi/ms2010.sf1.zip",
		},
		'mo': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Missouri/mo2010.sf1.zip",
		},
		'mt': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Montana/mt2010.sf1.zip",
		},
		'national': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/National/us2010.sf1.zip",
		},
		'ne': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Nebraska/ne2010.sf1.zip",
		},
		'nv': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Nevada/nv2010.sf1.zip",
		},
		'nh': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/New_Hampshire/nh2010.sf1.zip",
		},
		'nj': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/New_Jersey/nj2010.sf1.zip",
		},
		'nm': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/New_Mexico/nm2010.sf1.zip",
		},
		'ny': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/New_York/ny2010.sf1.zip",
			'mirror': "",
			'sha1': "",
			'dictionary': "",
		},
		'nc': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/North_Carolina/nc2010.sf1.zip",
		},
		'nd': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/North_Dakota/nd2010.sf1.zip",
		},
		'oh': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Ohio/oh2010.sf1.zip",
		},
		'ok': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Oklahoma/ok2010.sf1.zip",
		},
		'or': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Oregon/or2010.sf1.zip",
		},
		'pa': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Pennsylvania/pa2010.sf1.zip",
		},
		'pr': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Puerto_Rico/pr2010.sf1.zip",
		},
		'ri': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Rhode_Island/ri2010.sf1.zip",
		},
		'sc': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/South_Carolina/sc2010.sf1.zip",
		},
		'sd': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/South_Dakota/sd2010.sf1.zip",
		},
		'tn': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Tennessee/tn2010.sf1.zip",
		},
		'tx': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Texas/tx2010.sf1.zip",
		},
		'ut': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Utah/ut2010.sf1.zip",
		},
		'vt': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Vermont/vt2010.sf1.zip",
		},
		'va': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Virginia/va2010.sf1.zip",
		},
		'wa': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Washington/wa2010.sf1.zip",
		},
		'wv': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/West_Virginia/wv2010.sf1.zip",
		},
		'wi': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Wisconsin/wi2010.sf1.zip",
			'mirror': "",
			'sha1': "",
			'dictionary': "",
		},
		'wy': {
			'url': "http://www2.census.gov/census_2010/04-Summary_File_1/Wyoming/wy2010.sf1.zip",
		},
	}
	
	db_type = 'sql'

	def unpack():
		"""
		Overload unpack method to deal with files nmaed .sf1
		"""
		#import rename
		#rename 's/\.sf1$/\.txt/' *.sf1   #need to rename all the sf1 files to txts

		# call standard unpack
		Map.unpack()

	def install():
		"""
		Overload install method
		"""

		# Open SQL file from MS Access using MDBTOOLS and turn it into a SQL file
		# Make necessary modifications to SQL file and file names on unpacked system so install works properly
		# Run standard installer now with appropriate modifications in place
		Map.install()
	