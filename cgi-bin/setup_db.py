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
c.execute("CREATE TABLE IF NOT EXISTS completed_chores (id INTEGER PRIMARY KEY, name TEXT, chore TEXT, date TEXT, value TEXT);")
c.execute("CREATE TABLE IF NOT EXISTS chore_table (chore TEXT, value TEXT);")
c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT PRIMARY KEY, gauth TEXT, email TEXT);")
c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT PRIMARY KEY, gauth TEXT, email TEXT);")
c.execute("VACUUM;")
conn.commit()
c.close()
conn.close()

print "Content-type:text/html\r\n\r\n"
