#!/usr/bin/env python2.7
# Remember to change "python 2.7" to "python" -- this shouldn't be based on old version of Python

# MINER
# Dependencies: mdbtools, mysql (goal to move to any database), rename
 
# MIT License
# Name inspired by homebrew for Mac OS X 
# Project Goal: Automate the download, liberation, and "installation" of online but difficult to access data and open data 

import glob, os, csv, sys, getopt
from library.utils.helpers import *
from library.utils.db import *
from library.maps.uscensus import *


def main(argv):

    # parser = argparse.ArgumentParser(description="Use $miner --help for usage details")
    # parser.add_argument("-h", "--h", "-help", "--help")
    # parser.add_argument("-extract", "--extract")
    # args = parser.parse_args()

    # for arg in args:
    #     if arg in ("-h", "--h", "-help", "--help"):
    #         print "Usage:\n" +\
    #                 "  miner -search DATASET\n" +\
    #                 "  miner -assay DATASET (tell more about a dataset)\n" +\
    #                 "  miner -extract DATASET [--options]\n"
    #         sys.exit()

    #     elif opt in ("-extract"):
    #         proc = USCensus2010
    #         proc.install() 

    try:
        opts, args = getopt.getopt(argv,"he:", ["help","extract"])
    except getopt.GetoptError:
        print "Usage: $miner [args]\nCheck help for more details."
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--h", "-help", "--help"):
            print "Usage:\n" +\
                    "  miner -search DATASET\n" +\
                    "  miner -assay DATASET (tell more about a dataset)\n" +\
                    "  miner -extract DATASET [--options]\n"
            sys.exit()

        elif opt in ("-extract"):
            proc = USCensus2010()
            proc.install() 

if __name__ == "__main__":
   main(sys.argv[1:])

#from time import sleep  
#from random import random  
#from clint.textui import progress  
#if __name__ == '__main__':
#    for i in progress.bar(range(100)):
#        sleep(random() * 0.2)

#    for i in progress.dots(range(100)):
#        sleep(random() * 0.2)


#from clint.textui import colored
#print colored.green("HELLO BASH")

