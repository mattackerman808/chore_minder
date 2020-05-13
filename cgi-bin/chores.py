#!/bin/python

import cgi
import sqlite3
import datetime
import hashlib

print "Content-type:text/html\r\n\r\n"

sqlite_file = '/var/tmp/chores.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

print('''
<!DOCTYPE html>
<html>
<head>
<style>
div {
  margin-top: 100px;
  margin-bottom: 100px;
  margin-right: 150px;
  margin-left: 100px;
  font-family: "SF Pro Text", "Myriad Set Pro", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  font-size: 100%;
}
input, radio {
  font-family: "SF Pro Text", "Myriad Set Pro", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  font-size: 180%;
}
select, option {
  font-family: "SF Pro Text", "Myriad Set Pro", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  font-size: 180%;
}
</style>
<title>808 Chore Minder</title>
<body bgcolor=white>
<center>
<img src=/images/chores.jpg>
</center>
<div>
Select Your Name:<br><br>
<form action="/cgi-bin/submit.py">
  <input type="radio" name="name" value="ben" required> Ben<br>
  <input type="radio" name="name" value="jake"> Jake<br>
  <input type="radio" name="name" value="lucas"> Lucas<br>
  <br><br>
  Select your completed Chore:<br><br>
  <select id="chore" name="chore">
''')

c.execute('''SELECT chore FROM chore_table''')
chores = c.fetchall()

for chore in sorted(chores):
    chore_fixed = "%s" % chore
    print "<option value=\"%s\">%s" % (chore_fixed,chore_fixed)
    print "</option>"

print('''
</select>
  <br>
  <br>
  <input type="submit" style="font-size:100%;color:white;background-color:blue">
</form>
</div>
</form>

</body>
</html>
''')
