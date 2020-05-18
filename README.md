# chore_minder
Kids Chore Tracker

Simple CGI / Python to help track kids (or anyones) chores.

Install:

Currently requires python2 in /bin/python (will fix soon)

Requires sqllite DB libs for python install

* Clone into DocRoot
* Setup cgi-bin for execution within your web server
* Go to admin page (/cgi-bin/admin.py)
* Create a new chore
* Create a new user
* Go to main chore page (/cgi-bin/chores.py)
* Looks for REMOTE_USER env variable to ID user
* Create a user with REMOTE_USER tag (Gauth field, was written for Google auth intergration)
** will print variable under Guru data
* Start creating chores with values and have users submit them
