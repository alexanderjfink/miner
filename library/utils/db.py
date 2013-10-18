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

    self.db = dbapi2.connect(**config)
    
    # Create cursor
    self.cursor = db.cursor()

    return self.db


  def create_db(db_name=None, query=None, drop_if_exists=False):
    """
    Either want a database name or a full query to run through this abstracted method
    """

    # can't do this without db_name
    if drop_if_exists and db_name:
      self.cursor.execute("DROP DATABASE %s;" % db_name)

    if query:
      self.cursor.execute(query)
      self.cursor.commit()
      return True
    elif db_name:
      self.cursor.execute("CREATE DATABASE IF NOT EXISTS %s;" % db_name)
      self.cursor.commit()
      return True
    else:
      # fail if neither is specified
      return False
    

  def create_table(db_name=None, table_name=None, headers_types=None, query=None):
    """
    Generate a create table query on a database
    """

    if query:
      self.cursor.execute("USE %s;" % db_name)
      self.cursor.execute(query)
      self.cursor.commit()
      return True
    elif db_name and table_name and headers_types:
      self.cursor.execute("USE %s" % db_name)
      self.cursor.execute("CREATE TABLE %s (%s);" % (table_name, headers_types))
      self.cursor.commit()
      return True
    else:
      # something didn't work
      return False

  def insert(db_name=None, table_name=None, values=None, query=None):

    if query:
      # if here, we've been sent a pre-prepared query
      self.cursor.execute(query)
      self.cursor.commit()
      return True
    elif db_name and table_name and values:
      self.cursor.execute("USE %s;" % db_name)
      self.cursor.execute("INSERT INTO %s VALUES %s;" % (table_name, values))
      self.cursor.commit()
      return True
    else:
      # if here, we didn't get a query to run, so do what we need to...
      return False

  def query(db_name, query):
    if db_name and query:
      self.cursor.execute("USE %s;" % db_name)
      self.cursor.execute(query)
      self.cursor.commit()
      return True
    else:  
      # fail
      return False

  def commit():
    self.cursor.commit()
    self.cursor.close()
