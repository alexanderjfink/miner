"""
DATABASE ABSTRACTIONS
"""

import mysql.connector as dbapi2

class DBConnect: 
  # Function to connect to database
  # Abstract this eventually to make more DB options available
  def __init__(self):

    config = {
      'user': DATABASES['sql'].USERNAME,
      'password': DATABASES['sql'].PASSWORD,
      'host': DATABASES['sql'].HOSTNAME,
      'raise_on_warnings': False,
    }


    #try:
    self.db = dbapi2.connect(**config)
    return self.db
    
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

  def create_db():
    pass

  def create_table(db_name=None, table_name=None, query=None):
    if query:
      self.db.execute(query)
    else:
      pass

  def insert(db_name=None, table_name=None, values=None, query=None):

    if query:
      # if here, we've been sent a pre-prepared query
      self.db.execute(query)
    else:
      # if here, we didn't get a query to run, so do what we need to...


  def commit():
    self.cursor.commit()
    self.cursor.close()
