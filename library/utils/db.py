#########################
# DATABASE ABSTRACTIONS #
#########################

import mysql.connector as dbapi2

class DBConnect: 
  # Function to connect to database
  # Abstract this eventually to make more DB options available
  def connect(self):
      config = {
          'user': 'specialuser',
          'password': 'specialpass',
          'host': 'localhost',
          'raise_on_warnings': False,
      }


      #try:
      db = dbapi2.connect(**config)
      return db
      
      ## NEED TO FIX ERROR HANDLING HERE

      # except db.Error as err:
      #   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      #     print("Something is wrong with your user name or password")
      #    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      #      print("Database does not exist")
      #    else:
      #      print(err)
      #  else:
      #    cnx.close()

      
      # from mysql.connector import errorcode
      # try:
      #   cnx = mysql.connector.connect(**config)
      #   return cnx
      # except mysql.connector.Error as err:
      #   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      #     print("Something is wrong with your user name or password")
      #   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      #     print("Database does not exist")
      #   else:
      #     print(err)
      # else:
      #   cnx.close()