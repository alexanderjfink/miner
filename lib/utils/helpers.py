
####################
# HELPER FUNCTIONS #
####################

# Function to connect to database
# Abstract this eventually to make more DB options available
def db_connect():
    config = {
        'user': 'specialuser',
        'password': 'specialpass',
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