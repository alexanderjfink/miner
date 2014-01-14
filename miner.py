"""Miner.

Usage:
	miner.py search <dataset>
	miner.py (assay|describe) <dataset>
	miner.py (extract|install) <dataset>

Options:
	-h --help     Show this screen.
	--version     Show version.

"""

# External Libraries
from docopt import docopt

# Local libraries
from library.utils.helpers import *
from library.utils.db import *

# Temporary module imports
from library.maps.uscensus import *
from library.maps.usform990 import *
from library.maps.nycpolicepenalties import *


if __name__ == '__main__':
	args = docopt(__doc__, version='Miner 0.0.1a')
	
	# TODO:  SHOULD BUILD THIS MAP OUT OF A LISTING OF MAPS IN THE MAPS/ FOLDER
	maps = {
		'uscensus2010': USCensus2010,
		'usform990': USForm990Extracts,
		'nycpolicepenalties': NYCPolicePenalties,
	}

	# TODO: Should I switch this to a dictionary switching model from Learning Python?

	if args['install'] or args['extract']:
		# Try to extract the data.
		# Currently this involves running a "map" to the data, involving:
		# - download -- download the data from a server
		# - unpack -- unzip the data and clean it
		# - install -- send it to the configured database

		# need some **kwargs
		# install_location
		try:
			proc = maps[args['<dataset>']]()
			proc.setup()
			proc.download()
			proc.unpack()
			proc.install()
			# proc.cleanup()
		except KeyError:
			print "Can't find dataset. Try miner search <dataset>"
		else:
			print "Dataset " + args['<dataset>'] + " installed successfully."

	elif args['assay'] or args['describe']:
		try:
			proc = maps[args['<dataset>']]()
			print proc.description
			print proc.homepage
		except KeyError:
			print "Can't find dataset. Try miner search <dataset>"

	elif args['search']:
		# TODO: Need to add fuzzy searching of datasets
		try:
			proc = maps[args['<dataset>']]()
		except KeyError:
			print "Dataset does not exist. Add it by visiting http://www.github.com/alexanderjfink/miner"