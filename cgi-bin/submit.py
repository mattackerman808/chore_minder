#!/bin/python

import cgi
import sqlite3
import datetime

sqlite_file = '/var/tmp/chores.sqlite'

daytime = datetime.datetime.now()

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
  c.execute("CREATE TABLE IF NOT EXISTS completed_chores (id INTEGER PRIMARY KEY, name TEXT, chore TEXT, date TEXT, value TEXT);")
  c.execute("VACUUM;")
except:
  log.critical("Exception creating sqlite3 tables")
  exit(1)

form = cgi.FieldStorage()
name=form.getfirst("name", "").lower()
chore=form.getfirst("chore", "").lower()
date=daytime.strftime("%x")

c.execute('''SELECT value FROM chore_table WHERE chore=?''', (chore,))
value = c.fetchone()
value_fixed = "%s" % value

c.execute('''INSERT INTO completed_chores (name,chore,date,value) VALUES (?,?,?,?);''', (name,chore,date,value_fixed))

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
<title>Chore Submitter</title>
</head>
<body>
''')

print "<h4>Thanks %s!<br><br>I wrote down the chore: %s</h4>" % (name.capitalize(), chore.capitalize())

print('''
<a href="chores.py">Go Back</a>
</body>
</html>
''')
