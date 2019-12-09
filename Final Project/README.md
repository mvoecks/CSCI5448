# My Phish Stats #
##### Michael Voecks #####

### Required Python Modules ###
- ABC
- re
- heapq
- BeautifulSoup
- requests
- sqlite3

### Running the Code ###
BEFORE RUNNING ANY CODE, Ensure that you have a sqlite3 database named 'phishstats' in the code directory. This table must be configured with the following tables:
- CREATE TABLE Shows (date TEXT Primary Key, venue TEXT NOT NULL, location TEXT NOT NULL, footer TEXT);
- CREATE TABLE Songs (name TEXT NOT NULL, date TEXT NOT NULL, setName TEXT NOT NULL, songNumber INTEGER NOT NULL, description TEXT);
- CREATE TABLE Users (name TEXT, date TEXT);

This program uses the python console to display information and gather input from the user, so it is recommeded that it is run via the command line (linux) or via Powershell (windows). To start the program naviate to the Code folder and execute the command

_python ./runner.py
