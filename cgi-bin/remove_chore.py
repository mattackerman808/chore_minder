#!/bin/python

import cgi
import sqlite3

sqlite_file = '/var/tmp/chores.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

form = cgi.FieldStorage()
id=form.getfirst("id", "").lower()

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('''DELETE FROM completed_chores WHERE id = ?''', (id,))
c.execute("VACUUM;")

print "Content-type:text/html\r\n\r\n"

print('''
<!DOCTYPE html>
<html>
<head>
<title>Chore Remover</title>
</head>
<body>
''')

print "Deleted!<br><br><br>"

print('''
<a href="reporter.py">Go Back</a>
</body>
</html>
''')
