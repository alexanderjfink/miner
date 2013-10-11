""" 
miner map for NYC Police Department Penalties data
Data is released publicly by the City of New York
"""

from miner import *
import urllib2, gzip, re

class NYCPolicePenalties:
	description = 'US Non-Profit Form 990 Tax information released by CitizenAudit'
	homepage = 'http://data.cityofnewyork.us'


	# Place all download functionality in here, should download files to a standard download directory
	# Should check whether args have been specified for download. In this case, we might have something like
	# $miner extract uscensus --state=mn -- in this case, grab census data only for MN
	def download(self):

		# PLACEHOLDER: Change this to eventually be GLOBAL_CONSTANT_TEMPORARY_DIRECTORY
		os.chdir('./tmp/')

		# CODE FROM: http://stackoverflow.com/questions/9628770/how-can-i-download-a-file-to-a-specific-directory

		# URL should be main thing in here... abstract out the rest
		url = ("https://data.cityofnewyork.us/api/views/ns22-2dcm/rows.csv")
		file_name = url.split('/')[-1]

		try:
			os.makedirs(file_name + "_store")
		except OSError:
			print "Directory already exists for this file..."

		os.chdir("./" + file_name + "_store")

		if os.path.exists(file_name):
			print "Your lucky day! You already have a local copy of this file..."
		else:
			# Download file and display progress bar -- 
			# PLACEHOLDER: ABSTRACT into function somewhere, doesn't belong in a map
			u = urllib2.urlopen(url)
			f = open(file_name, 'wb')
			meta = u.info()
			file_size = int(meta.getheaders("Content-Length")[0])
			print "Downloading: %s Bytes: %s" % (file_name, file_size)

			file_size_dl = 0
			block_sz = 8192
			while True:
			    buffer = u.read(block_sz)
			    if not buffer:
			    	break

			    file_size_dl += len(buffer)
			    f.write(buffer)
			    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
			    status = status + chr(8)*(len(status)+1)
			    print status,

			f.close()

		return file_name

	# Place all unpacking functionality here. Unpacking should involve: 
	#   unzipping files,
	#   changing file names for consistency
	def unpack(self, file_name):
		print "Unpacking ..."

		# This file downloads as a sql.gz, need to unpack it.
		# os.system("gzip -d " + file_name)
		
		# rename .sf1 data files to .csv
		# consider replacing bash script w/python
		# run_script("rename 's/\.sf1$/\.csv/' *.sf1")
		return file_name


	# Place all installation functionality here. This involves:
	#   pulling files and sending data to database api for insertion
	def install(self, file_name):
		print "Installing..."
		#################################################################
		# POPULATE DATA TABLES 											#
		# For this formulae, use all CSV files in downloaded sf1 folder #
		#################################################################

		# open MySQL connection
		db = DBConnect()
		cnx = db.connect()

		# Create cursor
		cursor = cnx.cursor()

		# Create database if it isn't there already
		cursor.execute("DROP DATABASE IF EXISTS nycpolicepenalties;")
		cursor.execute("CREATE DATABASE IF NOT EXISTS nycpolicepenalties;")
		cursor.execute("USE nycpolicepenalties;")
		cnx.commit()

		# Need to create a SQL query that creates a table with the right column values
		create_table_query = "CREATE TABLE IF NOT EXISTS penatlies (year year, penalties text, officer_count int);"
	
		cursor.execute(create_table_query)
		cnx.commit()

		for files in glob.glob("*.csv"):
			# Need to first create the table

		    #GENERAL INSERT SQL
			add_csv_file = ('''INSERT INTO manifest VALUES (%(csv_row)s);''')
		    
		    # Open the CSV file and iterate it by row
		    # Yes, this is slower than using a LOAD DATA LOCAL INFILE SQL query (at least I'm pretty sure it is), but I'm not convinced
		    # that will work easily across all systems and it is not cross-database compatible
			with open(files, 'rb') as csvfile:
				next(csvfile)
				spamreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		        
		           
				# regex for date detection
				# got to do a bunch of stupid calendar stuff here
				a = re.compile("[0-1]?[0-9]/[0-2][0-9][0-9][0-9]")

				for row in spamreader:
		        
					csv_row = []
					for r in row:
						# because date field is in Month/Year, we need to detect and add a day

						# Detect if this CSV file's date...
						if a.match(r):
							month, year = r.split('/')
							r = year + "-" + month + "-01"
						
						to_append = is_number(r)

						csv_row.append(to_append)

					
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

	def cleanup(self):
		# Clean up extra stuffs here
		sys.exit()