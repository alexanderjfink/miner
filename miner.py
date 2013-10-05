#!/usr/bin/env python2.7
# Remember to change "python 2.7" to "python" -- this shouldn't be based on old version of Python

# MINER
# Dependencies: mdbtools, mysql (goal to move to any database), rename
 
import glob, os, csv, sys, getopt
from library.utils.helpers import *
from library.utils.db import *
from library.maps.uscensus import *


def main(argv):

    maps = {
        'uscensus2010': USCensus2010,
    }

    try:
        opts, args = getopt.getopt(argv,"he:a:s:", ["help","extract=","assay=","search="])
    except getopt.GetoptError:
        print "Usage: $miner [args]\nCheck help for more details."
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--h", "-help", "--help"):
            print "Usage:\n" +\
                    "  miner -s DATASET (search) \n" +\
                    "  miner -a DATASET (tell more about a dataset)\n" +\
                    "  miner -e DATASET [--options] (extract dataset)\n"
            sys.exit()

        elif opt in ("-e"):
            try:
                proc = maps[arg]()
                proc.install() 
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

