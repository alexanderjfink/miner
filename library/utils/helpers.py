"""
HELPER FUNCTIONS
Contained within are functions that help along the major functionality of the software
They are within a separate file because they can be abstracted to use elsewhere

Eventually this file should be parsed out into separate helper functions for different modules.

Each of these functions has corresponding tests in tests/helpers_test.py
"""

import os, csv, sys, optparse
from conf.settings import *
# from messytables import StringType, IntegerType, DateType, \
#         CSVTableSet, type_guess, \
#         types_processor, headers_guess, headers_processor, \
#         offset_processor, any_tableset

import messytables
import messy2sql
import urllib2

def download_file(url, with_progress_bar=True):
    """ Download file and display progress bar """

    file_name = url.split('/')[-1]
    
    if os.path.exists(file_name):
        print "Your lucky day! You already have a local copy of this file..."
    else:
        u = urllib2.urlopen(url)
        f = open(file_name, 'wb')

        if with_progress_bar:
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


# def csv_to_sql_table(csv_file, **kwargs):
#     """
#     Takes a CSV file as an object
#     Use csvkit's csvsql functionality to sniff out headers and build SQL
#     Returns a SQL CREATE TABLE statement

#     BUG DOES NOT YET DETECT DATETIME FIELDS,
#     MessyTables implementation of mine DID detect DATETIME fields, need to determine whether CSVKIT can find date/time variables as well
#     or whether to add the csvsql conversion functionality to MessyTables
#     """

#     fh = open(csv_file, 'rb')

#     # for now guess at assignments
#     snifflimit = None
#     blanks_as_nulls = False
#     infer_types = False
#     no_header_row = False
#     no_constraints = False
#     db_schema = ""
#     no_inference = False

#     # name the table after the file name
#     table_name = os.path.splitext(os.path.split(csv_file)[1])[0]

#     # debugging
#     if DEBUG:
#         print table_name

#     csv_table = table.Table.from_csv(
#         fh,
#         name = table_name,
#         snifflimit = snifflimit,
#         blanks_as_nulls = (not blanks_as_nulls),
#         infer_types = (not no_inference),
#         no_header_row = no_header_row,
#         **kwargs
#     )

#     fh.close()

#     metadata = None
#     sql_table = sql.make_table(
#             csv_table,
#             table_name,
#             no_constraints,
#             db_schema,
#             metadata
#         )

#     if DEBUG:
#         print sql.make_create_table_statement(sql_table, metadata)

#     return sql.make_create_table_statement(sql_table, metadata)

#     # if not self.args.no_create:
#     #     sql_table.create()

#     # if self.args.insert:
#     #     insert = sql_table.insert()
#     #     headers = csv_table.headers()

#     #     conn = engine.connect()
#     #     trans = conn.begin()
#     #     conn.execute(insert, [dict(zip(headers, row)) for row in csv_table.to_rows()])
#     #     trans.commit()
#     #     conn.close()

#     # # Writing to file
#     # else:
#     #     sql_table = sql.make_table(csv_table, table_name, self.args.no_constraints)
#     #     self.output_file.write((u'%s\n' % sql.make_create_table_statement(sql_table, dialect=self.args.dialect)).encode('utf-8'))




# def generate_rows(file_name):
#     """

#     """
#     sniffer = csv.Sniffer()
#     dialect = sniffer.sniff(file_name.readline())
#     file_name.seek(0)

#     reader = csv.reader(file_name, dialect)
#     for line in reader:
#         yield line

# def csv_to_sql(csv, insert_type):
#     """
#     Takes a CSV file as an object
#     insert_type is either single row at a time or all rows at once
#     """
#     opts, args = parse_options()

#     filename = args[0]

#     if filename == "-":
#         if opts.table is None:
#             print "ERROR: No table specified and stdin used."
#             raise SystemExit, 1
#         fd = sys.stdin
#         table = opts.table
#     else:
#         fd = open(filename, "rU")
#         if opts.table is None:
#             table = os.path.splitext(filename)[0]
#         else:
#             table = opts.table

#     rows = generate_rows(fd)

#     if opts.fields:
#         fields = ", ".join([x.strip() for x in opts.fields.split(",")])
#     else:
#         fields = ", ".join(rows.next())

#     for i, row in enumerate(rows):
#         if i in opts.skip:
#             continue

#         values = ", ".join(["\"%s\"" % x for x in row])
#         print "INSERT INTO %s (%s) VALUES (%s);" % (table, fields, values)

# if __name__ == "__main__":
#     main()