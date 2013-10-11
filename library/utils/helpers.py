"""
HELPER FUNCTIONS
Contained within are functions that help along the major functionality of the software
They are within a separate file because they can be abstracted to use elsewhere

Eventually this file should be parsed out into separate helper functions for different modules.

Each of these functions has corresponding tests in tests/helpers_test.py
"""

import os, csv, sys, optparse
from conf.settings import *
from messytables import StringType, IntegerType, DateType, \
        CSVTableSet, type_guess, \
        types_processor, headers_guess, headers_processor, \
        offset_processor, any_tableset



def csv_to_sql_table(csv_file):
    """
    Takes a CSV file as an object
    Sniff to see if first line is a header using messytables
    Returns a SQL CREATE TABLE statement
    """

    fh = open(csv_file, 'rb')
    table_name = os.path.splitext(csv_file)[0]

    # Load a file object:
    table_set = CSVTableSet(fh)

    # If you aren't sure what kind of file it is, you can use
    # any_tableset.
    #table_set = any_tableset(fh)

    # A table set is a collection of tables:
    row_set = table_set.tables[0]

    # A row set is an iterator over the table, but it can only
    # be run once. To peek, a sample is provided:
    # print row_set.sample.next()

    # guess header names and the offset of the header (some people put titles, etc. in first few lines):
    offset, headers = headers_guess(row_set.sample)
    row_set.register_processor(headers_processor(headers))

    # add one to begin with content, not the header:
    row_set.register_processor(offset_processor(offset + 1))

    # guess column types:
    types = type_guess(row_set.sample, strict=False)

    # and tell the row set to apply these types to
    # each row when traversing the iterator:
    # row_set.register_processor(types_processor(types))

    # need to declare types here because MessyTables builds its own typing...
    str_type = StringType()
    int_type = IntegerType()
    date_type = DateType('%d/%m/%Y')

    # need to iterate over these and switch MessyTable types to SQL db types
    # maybe abstract this to a function if necessary later
    # not all types are here yet, should fail on non-present types...
    conv_dict = {
        str_type: 'varchar(255)',
        int_type: 'int',
        date_type: 'date()'
    }

    # Need to iterate over the types found and create a string that will go into the SQL query 
    # in the form of 'column_name column_type, column_name column_type'
    # I don't know how to get an iterator here w/a different type for a "for iter, types list in types" doesn't work
    i=0
    insert_string = headers
    for t in types:
        insert_string[i] = headers[i] + " " + conv_dict[t]
        i += 1

    # Have to do a few final little things here... namely:
    # the string comes out looking like this
    # [u'id int', u'other varchar(255)']
    # therefore need to remove the unicode designator 'u' and the string quotes ''
    # needs to end up looking like: id int, other varchar
    # str() changes the list into one string
    # first replace() drops the unicode designator. we need u' to make sure we aren't dropping "u" in column names or data types
    # second replace() drops all the strings ''
    # strip() removes the brackets around the the list-turned-string
    final_types = str(insert_string).replace("u'", "'").replace("'","").strip('[]')
    sql_query = "CREATE TABLE %(table_name)s (%(types)s);" % {'table_name': table_name, 'types': final_types}

    if DEBUG:
        print sql_query

    return sql_query

    # now run some operation on the data:
    # for row in row_set:
    #   do_something(row)

def generate_rows(file_name):
    """

    """
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(file_name.readline())
    file_name.seek(0)

    reader = csv.reader(file_name, dialect)
    for line in reader:
        yield line

def csv_to_sql(csv, insert_type):
    """
    Takes a CSV file as an object
    insert_type is either single row at a time or all rows at once
    """
    opts, args = parse_options()

    filename = args[0]

    if filename == "-":
        if opts.table is None:
            print "ERROR: No table specified and stdin used."
            raise SystemExit, 1
        fd = sys.stdin
        table = opts.table
    else:
        fd = open(filename, "rU")
        if opts.table is None:
            table = os.path.splitext(filename)[0]
        else:
            table = opts.table

    rows = generate_rows(fd)

    if opts.fields:
        fields = ", ".join([x.strip() for x in opts.fields.split(",")])
    else:
        fields = ", ".join(rows.next())

    for i, row in enumerate(rows):
        if i in opts.skip:
            continue

        values = ", ".join(["\"%s\"" % x for x in row])
        print "INSERT INTO %s (%s) VALUES (%s);" % (table, fields, values)

if __name__ == "__main__":
    main()



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