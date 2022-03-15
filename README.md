# chore_minder
Kids Chore Tracker

Simple CGI / Python to help track kids (or anyones) chores.

Install:

Currently requires python2 in /bin/python (will fix soon)

Requires cgi and sqlite3 DB libs for python install

System writes DB file into /var/tmp (will need write access for web server user)

* Make html dir your docroot
* Setup cgi-bin dir for execution within your web server
* Run DB Setup Script: /cgi-bin/setup_db.py
* Go to main chore page (/)
* Looks for REMOTE_USER env variable to ID user, will get warning until user is created with correct variable
* Create a user with REMOTE_USER tag within admin page (Gauth field in DB, was written for Google auth intergration)
* Home page will print variable under 'Guru data' if unknown
* Start creating chores with values and have users submit them
* Use admin page to see history and amount owed
