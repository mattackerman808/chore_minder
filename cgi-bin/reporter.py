#!/bin/python

import cgi
import sqlite3
import datetime

sqlite_file = '/var/tmp/chores.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

print "Content-type:text/html\r\n\r\n"

print('''
<!DOCTYPE html>
<html>
<head>
<title>Completed Chores</title>
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
<img src=/images/chores.png width="35%" height="35%">
</center>
<div>
<b>Completed Chores</b><br><br>
<table>
 <tr>
  <th>Name</th>
  <th>Chore</th>
  <th>Date</th>
  <th>Value</th>
 </tr>
''')

c.execute('''SELECT id FROM completed_chores''')
ids = c.fetchall()

for id in sorted(ids):
 
   c.execute('''SELECT name FROM completed_chores WHERE id = ?''', (id))
   name = c.fetchone()
   name_fixed = "%s" % name

   c.execute('''SELECT chore FROM completed_chores WHERE id = ?''', (id))
   chore = c.fetchone()

   c.execute('''SELECT date FROM completed_chores WHERE id = ?''', (id))
   date = c.fetchone()

   c.execute('''SELECT value FROM completed_chores WHERE id = ?''', (id))
   value = c.fetchone()

   chore_fixed = "%s" % chore

   print "<tr>"
   print "<td>%s</td>" % name_fixed.capitalize()
   print "<td>%s</td>" % chore_fixed.capitalize()
   print "<td>%s</td>" % date
   print "<td style=\"text-align:right\">$%s</td>" % value
   print "</tr>"

print('''
</table><br>
</div>
<div>
<b>Totals</b>
<table>
 <tr>
  <th>Name</th>
  <th>Total Owed</th>
 </tr>
''')

c.execute('''SELECT name FROM users''')
users=c.fetchall()

for user in sorted(users):

   user_fixed = "%s" % user
   print "<tr>"
   print " <td>%s</td>" % user_fixed.capitalize()

   c.execute('''select SUM(value) FROM completed_chores WHERE name = ?''', (user_fixed.lower(),))
   total = c.fetchone()

   print "  <td style=\"text-align:right\">$%s" % total
   print "  </td>"
   print " </tr>"

print('''
</table>
</div>
<div>
<br>
<a href="delete_chores.py"><b>Delete All Chores</b></a>
</div>
<a href="admin.py">Go Back</a>
</body>
</html>
''')
