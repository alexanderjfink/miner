""" 
miner map for U.S. Census 2010 Minnesota database
"""

from miner import *

class USCensus2010:
	description = 'Data from the 2010 Dicennial US Census.'
	homepage = 'http://www.census.gov'


	# Place all download functionality in here, should download files to a standard download directory
	# Should check whether args have been specified for download. In this case, we might have something like
	# $miner extract uscensus --state=mn -- in this case, grab census data only for MN
	def download():
		## SERIES OF PLACEHOLDERS TO FIX FOR FINAL PROJECT ##
		# PLACEHOLDER: Download SF1 datafiles
		# PLACEHOLDER: Download 2003 Access Database from US Census (2003 b/c mdbtools can deal only w/Access JET3, 4
		# PLACEHOLDER: Test whether mdbtools is installed and works
		sys.exit()


	# Place all unpacking functionality here. Unpacking should involve: 
	#   unzipping files,
	#   changing file names for consistency
	def unpack():
		# PLACEHOLDER: Unzip SF1 datafiles
		# PLACEHOLDER: Create new database
		# PLACEHOLDER: Build tables based on guide database 
		
		# rename .sf1 data files to .csv
		# consider replacing bash script w/python
		# run_script("rename 's/\.sf1$/\.csv/' *.sf1")
		sys.exit()


	# Place all installation functionality here. This involves:
	#   pulling files and sending data to database api for insertion
	def install(self):
		#################################################################
		# POPULATE DATA TABLES 											#
		# For this formulae, use all CSV files in downloaded sf1 folder #
		#################################################################

		# open MySQL connection
		# open MySQL connection
		db = DBConnect()
		cnx = db.connect()

		# Create cursor
		cursor = cnx.cursor()

		# Create database if it isn't there already
		cursor.execute("DROP DATABASE IF EXISTS uscensus2010;")
		cursor.execute("CREATE DATABASE IF NOT EXISTS uscensus2010;")
		cursor.execute("USE uscensus2010;")
		cnx.commit()

		# sqlstr = """load data local infile '/Users/afink/Desktop/mn000012010.csv' into table SF1_00001 
		#     columns terminated by ',' 
		# 	optionally enclosed by '"' 
		# 	escaped by '"' 
		# 	lines terminated by '\n'
		# 	(FILEID, STUSAB, CHARITER, CIFSN, LOGRECNO, P0010001);"""

		# for each CSV file 
		# match csv file name to table
		# generate load data local infile query
		# run sql query
		# PLACEHOLDER:  if verbose, print results

		cursor = cnx.cursor()

		os.chdir("./tmp/mn2010.sf1/")
		for files in glob.glob("*.csv"):

		    #GENERAL INSERT SQL
		    add_csv_file = ('''INSERT INTO %(table_name)s VALUES (%(csv_row)s);''')
		    
		    # Open the CSV file and iterate it by row
		    # Yes, this is slower than using a LOAD DATA LOCAL INFILE SQL query (at least I'm pretty sure it is), but I'm not convinced
		    # that will work easily across all systems and it is not cross-database compatible
		    with open(files, 'rb') as csvfile:
		        spamreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		        for row in spamreader:
		    
		    		# basic detection of whether this should be treated as a string or not...
		            csv_row = []
		            for r in row:
		                csv_row.append(is_number(r))    
		                
		            # Insert CSV file information
		            csv_info = {
		                'table_name': 'SF1_' + files[2:-8],
		                'csv_row': str(csv_row).strip('[]'),
		            }
		            
		            query = add_csv_file % csv_info
		            
		            print query
		            
		            cursor.execute(query)
		            
		            # PLACEHOLDER: Add csv.next() or some feature to figure out what line we are on out of the total to build
		            # a progress bar that can indicate how much is complete.
		    
		# Make sure data is committed to the database
		# Waiting until end to commit means we don't get partial datasets inserted.
		cnx.commit()
		cursor.close()
		cnx.close()
	
