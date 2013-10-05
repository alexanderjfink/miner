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
		                
		            # Insert CSV file information
		            csv_info = {
		                'table_name': 'SF1_' + files[2:-8],
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
	
