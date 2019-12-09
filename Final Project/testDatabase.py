import sqlite3

conn = sqlite3.connect('phishstats')
c = conn.cursor()
#date = '1994-12-29'
date = '2017-09-01'
name = 'Mike'

c.execute('SELECT * FROM Users WHERE name = ?', [name])
for element in c.fetchall():
    print(element[1])



'''
c.execute('SELECT * FROM Songs WHERE Date=? ORDER BY setName, songNumber', [date])
songInfo = c.fetchall()
for song in songInfo:
    print(song[0])

date = "2017-09-01"
venue = "Dick's"
location = "Commerce City, CO, USA"
footer = ''

statement = "INSERT INTO Shows (date, venue, location, footer) VALUES (?, ?, ?, ?);"
c.execute(statement, [date, venue, location, footer])
conn.commit()
'''
