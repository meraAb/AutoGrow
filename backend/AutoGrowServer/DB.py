import MySQLdb 

########################################################################
## Connect to Local DataBase

DB_HOST = 'localhost'
DB_USER = 'chris'
DB_PASSWORD = 'cdelis1994'
DB_NAME = 'AutoGrow'

# Create connection and database cursor objects

try:
  Connection = MySQLdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME,charset='utf8',use_unicode=False)
  Cursor = Connection.cursor()
except:
  print 'Cannot connect to DB'
  print 'Server will now exit'
  raise

