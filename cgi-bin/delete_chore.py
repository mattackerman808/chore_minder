#!/bin/python

import cgi
import sqlite3

sqlite_file = '/var/tmp/chores.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

form = cgi.FieldStorage()
chore=form.getfirst("chore", "").lower()

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute("PRAGMA auto_vacuum = 2;")
c.execute("PRAGMA encoding = 'UTF-8';")
c.execute("PRAGMA temp_store = MEMORY;")
c.execute("PRAGMA journal_mode = MEMORY;")
c.execute('''DELETE FROM chore_table WHERE chore = ?''', (chore,))
c.execute("VACUUM;")

print "Content-type:text/html\r\n\r\n"

print('''
<!DOCTYPE html>
<html>
<head>
<title>Chore Deleter</title>
</head>
<body>
''')

print "%s deleted!<br><br><br>" % chore

print('''
<a href="chore_manage.py">Go Back</a>
</body>
</html>
''')
