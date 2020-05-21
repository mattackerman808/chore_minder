#!/bin/python

import cgi
import sqlite3
import datetime

sqlite_file = '/var/tmp/chores.sqlite'

daytime = datetime.datetime.now()

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute("PRAGMA auto_vacuum = 2;")
c.execute("PRAGMA encoding = 'UTF-8';")
c.execute("PRAGMA temp_store = MEMORY;")
c.execute("PRAGMA journal_mode = MEMORY;")
c.execute("CREATE TABLE IF NOT EXISTS chore_table (chore TEXT, value TEXT);")
c.execute("VACUUM;")

print "Content-type:text/html\r\n\r\n"

print ('''
<!DOCTYPE html>
<html>
<head>
<title>Chore Admin</title>
</head>
<style>
 table, th, td { 
  border: 1px solid black; padding: 3px;
 }
 div {
  margin-top: 25px;
  margin-bottom: 25px;
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
<b>Current Chores Setup</b><br><br>

<table>
 <tr>
  <th>Chore</th>
  <th>Value</th>
 </tr>
''')

c.execute('''SELECT chore FROM chore_table''')
chores = c.fetchall()

for chore in sorted(chores):
 
   c.execute('''SELECT value FROM chore_table WHERE chore = ?''', (chore))
   value = c.fetchone()

   chore_fixed = "%s" % chore

   print "<tr>"
   print "<td>%s</td>" % chore_fixed.capitalize()
   print "<td style=\"text-align:right\">$%s</td>" % value
   print "</tr>"

print('''

</table>
</div>

<div>
<b>Add new:</b><br><br>
<form action="/cgi-bin/new_chore.py">
 Chore:<input type="text" name="chore" required><br>
 Value:&nbsp<input type="text" name="value" required><br><br>
 <input type="submit" style="font-size:100%;color:white;background-color:blue">
</form>
</div>

<div>
<b>Delete Chore</b><br><br>
<form action="/cgi-bin/delete_chore.py">
<select id="chore" name="chore">
''')

c.execute('''SELECT chore FROM chore_table''')
chores = c.fetchall()

for chore in sorted(chores):
    chore_fixed = "%s" % chore
    print "<option value=\"%s\">%s" % (chore_fixed,chore_fixed.capitalize())
    print "</option>"

print('''
</select>
  <br>
  <br>
  <input type="submit" style="font-size:100%;color:white;background-color:blue">
</form>
</div>

<div>
<a href="reporter.py">Run Payroll</a>
</div>

<div>
<a href="user_manage.py">Manage Users</a>
</div>

</body>
</html>
''')
