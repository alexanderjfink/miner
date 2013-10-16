#!/usr/bin/env python2.7
# Remember to change "python 2.7" to "python" -- this shouldn't be based on old version of Python

"""
MINER
Dependencies: mdbtools, mysql (goal to move to any database), rename (update list)

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
        # Should I switch this to a dictionary switching model from Learning Python?

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
            try:
                proc = maps[arg]()
            except KeyError:
                print "Dataset does not exist. Add it by visiting http://www.github.com/alexanderjfink/miner"

if __name__ == "__main__":
   main(sys.argv[1:])

