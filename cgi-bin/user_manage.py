#!/bin/python

import cgi
import sqlite3
import datetime

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

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Chore Minder Users</title>"
print "</head>"
print "<style> table, th, td { border: 1px solid black; padding: 3px;}</style>"
print '<style> div { margin-top: 5px; margin-bottom: 10px; margin-right: 150px; margin-left: 100px; font-family: "SF Pro Text", "Myriad Set Pro", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif; font-size: 100%; }</style>'
print "<body>"
print "<center>"
print '<img src=/images/chores.jpg>'
print "</center>"
print "<div>"
print "<b>Configured Users</b><br><br>"

c.execute('''SELECT name FROM users''')
names = c.fetchall()

print "<table>"
print " <tr>"
print "  <th>Name</th>"
print "  <th>Gauth</th>"
print "  <th>Email</th>"
print " </tr>"

for name in sorted(names):
 
   c.execute('''SELECT gauth FROM users WHERE name = ?''', (name))
   gauth = c.fetchone()

   c.execute('''SELECT email FROM users WHERE name = ?''', (name))
   email = c.fetchone()

   print "<tr>"
   print "<td>%s</td>" % name
   print "<td>%s</td>" % gauth
   print "<td>%s</td>" % email
   print "</tr>"

print "</table><br>"

print '<a href="admin.py">Go Back</a>'

print "</body>"
print "</html>"
