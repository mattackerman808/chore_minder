#!/bin/python

import cgi
import sqlite3
import datetime

sqlite_file = '/var/tmp/chores.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Completed Chores</title>"
print "</head>"
print "<style> table, th, td { border: 1px solid black; padding: 3px;}</style>"
print '<style> div { margin-top: 5px; margin-bottom: 10px; margin-right: 150px; margin-left: 100px; font-family: "SF Pro Text", "Myriad Set Pro", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif; font-size: 100%; }</style>'
print "<body>"
print "<center>"
print '<img src=/images/chores.jpg>'
print "</center>"
print "<div>"
print "<b>Completed Chores</b><br><br>"

c.execute('''SELECT id FROM completed_chores''')
ids = c.fetchall()

print "<table>"
print " <tr>"
print "  <th>Name</th>"
print "  <th>Chore</th>"
print "  <th>Date</th>"
print "  <th>Value</th>"
print " </tr>"

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

print "</table><br>"

print "</div><div>"
print "<b>Totals</b>"
print "<table>"
print " <tr>"
print "  <th>Name</th>"
print "  <th>Total Owed</th>"
print " </tr>"

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

print "</table>"
print "</div>"
print "<div>"
print "<br>"
print '<a href="delete_chores.py"><b>Delete All Chores</b></a>'
print "</div>"

print '<a href="admin.py">Go Back</a>'

print "</body>"
print "</html>"
