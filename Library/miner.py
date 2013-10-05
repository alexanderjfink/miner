#!/usr/bin/env python2.7
# Remember to change "python 2.7" to "python" -- this shouldn't be based on old version of Python

# MINER
# Dependencies: mdbtools, mysql (goal to move to any database), rename
 
# MIT License
# Name inspired by homebrew for Mac OS X 
# Project Goal: Automate the download, liberation, and "installation" of online but difficult to access data and open data 

# Current Goals: 
# Develop Python Formulae (Script) to Automate Liberation of US Census Summary Files

# Using mysql.connector provided by Oracle (yeck, Oracle)
import mysql.connector, glob, os, csv, sys, getopt


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

####################
# HELPER FUNCTIONS #
####################

# Function to connect to database
# Abstract this eventually to make more DB options available
def db_connect():
    config = {
        'user': 'user',
        'password': 'pass',
        'host': 'localhost',
        'database': 'uscensus',
        'raise_on_warnings': True,
    }
    
    from mysql.connector import errorcode
    try:
      cnx = mysql.connector.connect(**config)
      return cnx
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
      cnx.close()

# Test if string or #
def is_number(s):
    try:
        float(s)
        return float(s)
    except ValueError:
        return s
        
# Functions to run bash from Python
# From Ian Bicking, http://stackoverflow.com/a/2654398/1608991
def run_script(script, stdin=None):
    """Returns (stdout, stderr), raises error on non-zero return code"""
    import subprocess
    # Note: by using a list here (['bash', ...]) you avoid quoting issues, as the
    # arguments are passed in exactly this order (spaces, quotes, and newlines won't
    # cause problems):
    proc = subprocess.Popen(['bash', '-c', script],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        stdin=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if proc.returncode:
        raise ScriptException(proc.returncode, stdout, stderr, script)
    return stdout, stderr

# Functions to run bash from Python
# From Ian Bicking, http://stackoverflow.com/a/2654398/1608991
class ScriptException(Exception):
    def __init__(self, returncode, stdout, stderr, script):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr
        Exception.__init__('Error in script')
        
        
########################
# END HELPER FUNCTIONS #
########################

## SERIES OF PLACEHOLDERS TO FIX FOR FINAL PROJECT ##
# PLACEHOLDER: Download SF1 datafiles
# PLACEHOLDER: Unzip SF1 datafiles
# PLACEHOLDER: Download 2003 Access Database from US Census (2003 b/c mdbtools can deal only w/Access JET3, 4
# PLACEHOLDER: Test whether mdbtools is installed and works

# PLACEHOLDER: Create new database
# PLACEHOLDER: Build tables based on guide database 
## END PLACEHOLDERS

#################################################################
# POPULATE DATA TABLES 						#
# For this formulae, use all CSV files in downloaded sf1 folder #
#################################################################

# rename .sf1 data files to .csv
# consider replacing bash script w/python
run_script("rename 's/\.sf1$/\.csv/' *.sf1")

# open MySQL connection
cnx = db_connect()

sqlstr = """load data local infile '/Users/afink/Desktop/mn000012010.csv' into table SF1_00001 
    columns terminated by ',' 
	optionally enclosed by '"' 
	escaped by '"' 
	lines terminated by '\n'
	(FILEID, STUSAB, CHARITER, CIFSN, LOGRECNO, P0010001);"""

# for each CSV file 
# match csv file name to table
# generate load data local infile query
# run sql query
# PLACEHOLDER:  if verbose, print results

cursor = cnx.cursor()

os.chdir("./")
for files in glob.glob("*.csv"):

    #GENERAL INSERT SQL
    add_csv_file = ('''INSERT INTO %(table_name)s VALUES (%(csv_row)s);''')
    
    # Open the CSV file and iterate it by row
    # Yes, this is slower than using a LOAD DATA LOCAL INFILE SQL query (at least I'm pretty sure it is), but I'm not convinced
    # that will work easily across all systems and it is not cross-database compatible
    with open(files, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in spamreader:
    
    
            csv_row = []
            for r in row:
                csv_row.append(is_number(r))
            
            if 'mod' in files:
                table_name = 'SF1_' + files[2:-8] + 'mod'
            else:
                table_name = 'SF1_' + files[2:-8]
                
            # Insert CSV file information
            csv_info = {
                'table_name': table_name,
                'csv_row': str(csv_row).strip('[]'),
            }
            
            query = add_csv_file % csv_info
            
            if (debug):
                print query
            
            cursor.execute(query)
            
            # PLACEHOLDER: Add csv.next() or some feature to figure out what line we are on out of the total to build
            # a progress bar that can indicate how much is complete.
    
# Make sure data is committed to the database
# Waiting until end to commit means we don't get partial datasets inserted.
cnx.commit()
cursor.close()
cnx.close()

