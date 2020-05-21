#!/bin/python

import cgi
import sqlite3

sqlite_file = '/var/tmp/chores.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute("PRAGMA auto_vacuum = 2;")
c.execute("PRAGMA encoding = 'UTF-8';")
c.execute("PRAGMA temp_store = MEMORY;")
c.execute("PRAGMA journal_mode = MEMORY;")
c.execute("CREATE TABLE IF NOT EXISTS chore_table (chore TEXT, value TEXT);")
c.execute("VACUUM;")

form = cgi.FieldStorage()
chore=form.getfirst("chore", "").lower()
value=form.getfirst("value", "").lower()

if not chore:
    print "ERROR: No Chore Passed"
    exit(0)

if not value:
    print "ERROR: No Value"
    exit(0)

c.execute('''INSERT INTO chore_table (chore,value) VALUES (?,?);''', (chore,value))

conn.commit()
c.close()
conn.close()

print "Content-type:text/html\r\n\r\n"

print('''
<!DOCTYPE html>
<html>
<head>
<title>Chore Submitter</title>
</head>
<body>
''')

print "%s submitted!<br><br><br>" % chore

print('''
<a href="admin.py">Go Back</a>
</body>
</html>
''')
