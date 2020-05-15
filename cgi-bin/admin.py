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
  c.execute("CREATE TABLE IF NOT EXISTS chore_table (chore TEXT, value TEXT);")
  c.execute("VACUUM;")
except:
  log.critical("Exception creating sqlite3 tables")
  exit(1)

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Chore Admin</title>"
print "</head>"
print "<style> table, th, td { border: 1px solid black; padding: 3px;}</style>"
print '<style> div { margin-top: 25px; margin-bottom: 25px; margin-right: 150px; margin-left: 100px; font-family: "SF Pro Text", "Myriad Set Pro", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif; font-size: 100%; }</style>'
print "<body>"
print "<center>"
print '<img src=/images/chores.jpg>'
print "</center>"
print "<div>"
print "<b>Current Chores Setup</b><br><br>"

c.execute('''SELECT chore FROM chore_table''')
chores = c.fetchall()

print "<table>"
print " <tr>"
print "  <th>Chore</th>"
print "  <th>Value</th>"
print " </tr>"

for chore in sorted(chores):
 
   c.execute('''SELECT value FROM chore_table WHERE chore = ?''', (chore))
   value = c.fetchone()
   print "<tr>"
   print "<td>%s</td>" % chore
   print "<td style=\"text-align:right\">$%s</td>" % value
   print "</tr>"

print "</table>"
print "</div>"
print "<div>"
print "<b>Add new:</b><br><br>"
print '<form action="/cgi-bin/new_chore.py">'
print 'Chore:<input type="text" name="chore" required><br>'
print 'Value:&nbsp<input type="text" name="value" required><br><br>'
print '<input type="submit" style="font-size:100%;color:white;background-color:blue">'
print '</form>'
print '</div>'

print '<div>'
print '<b>Delete Chore</b><br><br>'
print '<form action="/cgi-bin/delete_chore.py">'

c.execute('''SELECT chore FROM chore_table''')
chores = c.fetchall()

print '<select id="chore" name="chore">'

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

<div>
<a href="reporter.py">Run Payroll</a>
</div>

</body>
</html>
''')
