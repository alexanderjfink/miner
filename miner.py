"""
MINER
Dependencies: mdbtools, postgresql (goal to move to any database), rename (update list)

Test Dependencies: nose
"""
 
import glob, os, csv, sys, getopt
from library.utils.helpers import *
from library.utils.db import *
from library.maps.uscensus import *
from library.maps.usform990 import *
from library.maps.nycpolicepenalties import *


def main(argv):

    # dict of existing maps
    # maps must be here in order to work

    # TODO:  SHOULD BUILD THIS MAP OUT OF A LISTING OF MAPS IN THE MAPS/ FOLDER
    maps = {
        'uscensus2010': USCensus2010,
        'usform990': USForm990,
        'nycpolicepenalties': NYCPolicePenalties,
    }

    try:
        opts, args = getopt.getopt(argv,"he:a:s:", ["help","extract=","assay=","search="])
    except getopt.GetoptError:
        print "Usage: $miner [args]\nCheck help for more details."
        sys.exit()

    for opt, arg in opts:
        # TODO: Should I switch this to a dictionary switching model from Learning Python?

        if opt in ("-h", "--h", "-help", "--help"):
            print "Usage:\n" +\
                    "  miner -s DATASET (search) \n" +\
                    "  miner -a DATASET (tell more about a dataset)\n" +\
                    "  miner -e DATASET [--options] (extract dataset)\n"
            sys.exit()

        elif opt in ("-e"):
            # Try to extract the data.
            # Currently this involves running a "map" to the data, involving:
            # - download -- download the data from a server
            # - unpack -- unzip the data and clean it
            # - install -- send it to the configured database

            # need some **kwargs
            # install_location
            try:
                proc = maps[arg]()
                file_name = proc.download()
                if file_name:
                    if proc.unpack(file_name):
                        if proc.install(file_name):
                            print "Dataset " + arg + " installed successfully."
                print "Dataset " + arg + " installed successfully"

            except KeyError:
                print "Can't find dataset. Try miner -s DATASET"


        elif opt in ("-a"):
            try:
                proc = maps[arg]()
                print proc.description
                print proc.homepage
            except KeyError:
                print "Can't find dataset. Try miner -s DATASET"

        elif opt in ("-s"):
            # TODO: Need to add fuzzy searching of datasets
            try:
                proc = maps[arg]()
            except KeyError:
                print "Dataset does not exist. Add it by visiting http://www.github.com/alexanderjfink/miner"


if __name__ == "__main__":
    """ Just runs the main function by default when this module is loaded """

    # Sends arguments from command line interface (CLI) to main function
    main(sys.argv[1:])

