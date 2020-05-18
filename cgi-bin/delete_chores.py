#!/bin/python

import sqlite3

sqlite_file = '/var/tmp/chores.sqlite'

try:
  conn = sqlite3.connect(sqlite_file)
  c = conn.cursor()
except:
  log.critical("Error creating sqlite3 DB file")
  exit(1)

try:
  c.execute("PRAGMA auto_vacuum = 2;")
  c.execute("PRAGMA encoding = 'UTF-8';")
  c.execute("PRAGMA temp_store = MEMORY;")
  c.execute("PRAGMA journal_mode = MEMORY;")
  c.execute("DROP TABLE IF EXISTS completed_chores")
  c.execute("CREATE TABLE IF NOT EXISTS completed_chores (id INTEGER PRIMARY KEY, name TEXT, chore TEXT, date TEXT, value TEXT);")
  c.execute("VACUUM;")
except:
  log.critical("Exception creating sqlite3 tables")
  exit(1)

print "Content-type:text/html\r\n\r\n"

print('''
<!DOCTYPE html>
<html>
<head>
<title>Chore Deleter</title>
</head>
<body>
All Completed Chores Deleted!<br><br><br>
<a href="admin.py">Go to Admin</a>
</body>
</html>
''')
