#!/bin/python

import cgi
import sqlite3

sqlite_file = '/var/tmp/chores.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

form = cgi.FieldStorage()
chore=form.getfirst("chore", "").lower()

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
  c.execute('''DELETE FROM chore_table WHERE chore = ?''', (chore,))
  c.execute("VACUUM;")
except:
  log.critical("Exception creating sqlite3 tables")
  exit(1)

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Chore Deleter</title>"
print "</head>"
print "<body>"
print "%s deleted!<br><br><br>" % chore
print '<a href="admin.py">Go Back</a>'
print "</body>"
print "</html>"

