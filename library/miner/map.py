"""
The basic form of a Map...
Should be general enough that it can fit all maps (unless there seems good reason to ignore this)
Should be specific enough that it does a lot of the heavy lifting for Maps
"""

class Map:

	# URL for homepage of dataset (e.g. http://census.gov/)
	homepage = ''

	# Specific URLs for the dataset downloads
	url = []

	# Mirror in case this dataset goes down
	mirror = []

	# sha1 checksum for dataset download
	sha1 = []

	# URLs for the data dictionaries
	dictionary = []

	# type of database to install ('docstore','sql','keyvalue')
	database_type = ''

	# Methods internal to Maps class

	def is_installed(self, map):
		"""
		Check if Map is already installed somewhere
		"""
		pass

	# These are the main methods used by maps
	def download(self):
		pass

	def unpack(self):
		pass

	def install(self):
		pass

	def cleanup(self):
		pass
	