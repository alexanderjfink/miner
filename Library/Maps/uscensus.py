# miner map for U.S. Census data

class USCensus2010:
	homepage = 'http://www.census.gov'

	# Place all download functionality in here, should download files to a standard download directory
	# Should check whether args have been specified for download. In this case, we might have something like
	# $miner extract uscensus --state=mn -- in this case, grab census data only for MN
	def download():


	# Place all unpacking functionality here. Unpacking should involve: 
	#   unzipping files,
	#   changing file names for consistency
	def unpack():


	# Place all installation functionality here. This involves:
	#   pulling files and sending data to database api for insertion
	def install():
	
