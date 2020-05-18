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

print('''
<!DOCTYPE html>
<html>
<head>
<title>Chore Minder Users</title>
</head>
<style>
 table, th, td {
  border: 1px solid black;
  padding: 3px;
  }
 div {
  margin-top: 5px;
  margin-bottom: 10px;
  margin-right: 150px;
  margin-left: 100px;
  font-family: "SF Pro Text", "Myriad Set Pro", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  font-size: 100%;
  }
</style>
<body>
<center>
<img src=/images/chores.jpg>
</center>
<div>
<b>Configured Users</b><br><br>
<table>
 <tr>
  <th>Name</th>
  <th>Gauth</th>
  <th>Email</th>
 </tr>
''')

c.execute('''SELECT name FROM users''')
names = c.fetchall()

for name in sorted(names):
 
   c.execute('''SELECT gauth FROM users WHERE name = ?''', (name))
   gauth = c.fetchone()

   c.execute('''SELECT email FROM users WHERE name = ?''', (name))
   email = c.fetchone()

   name_fixed = "%s" % name

   print "<tr>"
   print "<td>%s</td>" % name_fixed.capitalize()
   print "<td>%s</td>" % gauth
   print "<td>%s</td>" % email
   print "</tr>"

print('''
</table><br>
</div>
<div>
<b>Add New User</b>
<form action="/cgi-bin/new_user.py">
Name:<input type="text" name="name" required><br>
Gauth:<input type="text" name="gauth" required><br>
Email:&nbsp<input type="text" name="email" required><br><br>
<input type="submit" style="font-size:100%;color:white;background-color:blue">
</form>
</div>
<div>
<b>Delete User</b><br><br>
<form action="/cgi-bin/delete_user.py">
''')

c.execute('''SELECT name FROM users''')
names = c.fetchall()

print '<select id="user" name="user">'

for name in sorted(names):
    name_fixed = "%s" % name
    print "<option value=\"%s\">%s" % (name_fixed,name_fixed.capitalize())
    print "</option>"

print('''
</select>
  <br>
  <br>
  <input type="submit" style="font-size:100%;color:white;background-color:blue">
</form>
</div>
<a href="admin.py">Go Back</a>
</body>
</html>
''')
