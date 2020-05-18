#!/bin/python

import cgi
import sqlite3
import datetime
import os

print "Content-type:text/html\r\n\r\n"

sqlite_file = '/var/tmp/chores.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

username = os.environ.get('REMOTE_USER')

print('''
<!DOCTYPE html>
<html>
<head>
<style>
div {
  margin-top: 50px;
  margin-bottom: 50px;
  margin-right: 150px;
  margin-left: 100px;
  font-family: "SF Pro Text", "Myriad Set Pro", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  font-size: 100%;
}
input, radio {
  font-family: "SF Pro Text", "Myriad Set Pro", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  font-size: 100%;
}
select, option {
  font-family: "SF Pro Text", "Myriad Set Pro", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  font-size: 100%;
}
table, th, td {
  border: 1px solid black; 
  padding: 3px;
}
</style>
<title>808 Chore Minder</title>
<body bgcolor=white>
<center>
<img src=/images/chores.png width="35%" height="35%">
</center>
''')

c.execute('''SELECT name FROM users WHERE gauth = ?''', (username,))
realname = c.fetchone()

print "<div>"

if not realname:
   print "<h1>I don't know who you are yet!</h1><br>Ask your admin to create your account.<br><br><br>"
   print "Guru data: %s" % username
   print "</div></body></html>"
   exit(0)

realname_fixed = "%s" % realname

print "<h2>Hi there %s!</h2>What chore did you do?<br><br>" % realname_fixed.capitalize()

print '<form action="/cgi-bin/submit.py">'
print '<input type="hidden" name="name" value="%s" required>' % realname

c.execute('''SELECT chore FROM chore_table''')
chores = c.fetchall()

print '<select id="chore" name="chore">'

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
<h3>Your completed chores so far:</h3>
<table>
 <tr>
  <th>Chore</th>
  <th>Date</th>
  <th>Earned</th>
 </tr>
''')

realname_fixed = "%s" % realname

c.execute('''SELECT id FROM completed_chores WHERE name=?''', (realname_fixed.lower(),))
ids=c.fetchall()

for id in sorted(ids):

   c.execute('''SELECT chore FROM completed_chores WHERE id = ?''', (id))
   chore = c.fetchone()

   c.execute('''SELECT date FROM completed_chores WHERE id = ?''', (id))
   date = c.fetchone()

   c.execute('''SELECT value FROM chore_table WHERE chore = ?''', (chore))
   value = c.fetchone()

   chore_fixed = "%s" % chore

   print "<tr>"
   print "<td>%s</td>" % chore_fixed.capitalize()
   print "<td>%s</td>" % date
   print "<td style=\"text-align:right\">$%s</td>" % value
   print "</tr>"

print('''
</table>
</div>
<div>
<h3>Available Chores:</h3>
<table>
 <tr>
  <td>Chore</td>
  <td>Value</td>
 </tr>
''')

c.execute('''SELECT chore FROM chore_table''')
chores=c.fetchall()

for chore in sorted(chores):

   c.execute('SELECT value FROM chore_table WHERE chore = ?''', (chore))
   value=c.fetchone()

   chore_fixed = "%s" % chore

   print "<tr>"
   print "<td>%s</td>" % chore_fixed.capitalize()
   print "<td style=\"text-align:right\">$%s</td>" % value

print('''
</table>
</div>
</body>
</html>
''')
