#!/bin/python

import cgi
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
  c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT PRIMARY KEY, gauth TEXT, email TEXT);")
  c.execute("VACUUM;")
except:
  log.critical("Exception creating sqlite3 tables")
  exit(1)

form = cgi.FieldStorage()
name=form.getfirst("name", "").lower()
gauth=form.getfirst("gauth", "").lower()
email=form.getfirst("email", "").lower()

c.execute('''INSERT INTO users (name,gauth,email) VALUES (?,?,?);''', (name,gauth,email))

try:
  conn.commit()
  c.close()
  conn.close()
except:
  log.critical("Exception while commiting or closing database")

print "Content-type:text/html\r\n\r\n"

print('''
<!DOCTYPE html>
<html>
<head>
<title>User Creator</title>
</head>
<body>
''')

print "%s created!<br><br><br>" % name.capitalize()

print('''
<a href="user_manage.py">Go Back</a>
</body>
</html>
''')
