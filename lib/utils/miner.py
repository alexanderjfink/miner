#!/usr/bin/env python2.7
# Remember to change "python 2.7" to "python" -- this shouldn't be based on old version of Python

# MINER
# Dependencies: mdbtools, mysql (goal to move to any database), rename
 
# MIT License
# Name inspired by homebrew for Mac OS X 
# Project Goal: Automate the download, liberation, and "installation" of online but difficult to access data and open data 

import mysql.connector, glob, os, csv, sys, getopt
from utils.helpers import *


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"h", ["help"])
    except getopt.GetoptError:
        print "Usage: $miner [args]\nCheck help for more details."
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--h", "-help", "--help", "--h", "help"):
            print """Usage:
  miner search DATASET
  miner assay DATASET (tell more about a dataset)
  miner extract DATASET [--options]"""
            sys.exit()

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

