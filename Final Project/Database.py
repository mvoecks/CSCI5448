import sqlite3
import Show

class Database():
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName)
        self.c = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def loadUser(self, name):
        self.c.execute('SELECT * FROM Users WHERE name = ?', [name])
        shows = self.c.fetchall()
        if shows == []:
            return -1
        else:
            showlist = []
            for date in shows:
                showlist.append(date[1])
            return showlist

    def inDatabase(self, date):
        self.c.execute('SELECT * FROM Shows WHERE Date = ?', [date])
        if self.c.fetchone() == None:
            return False
        else:
            return True

    def getShowFromDatabase(self, date):
        self.c.execute('SELECT * FROM Shows WHERE Date = ?', [date])
        showInfo = self.c.fetchone()
        if showInfo != None:
            showList = {}
            showList['date'] = showInfo[0]
            showList['venue'] = showInfo[1]
            showList['location'] = showInfo[2]
            showList['footer'] = showInfo[3].split(',')

            self.c.execute('SELECT * FROM Songs WHERE Date=? ORDER BY setName, songNumber', [date])
            songInfo = self.c.fetchall()
            setlist = {}
            for song in songInfo:
                tempSong = Show.Song(song[0], songDesc = song[4])
                if song[2] in setlist:
                    setlist[song[2]].append(tempSong)
                else:
                    setlist[song[2]] = [tempSong]
            showList['setlist'] = setlist
            if 'set3' in setlist:
                return Show.ThreeSetShow(None, fromList = showList)
            elif 'set2' in setlist:
                return Show.TwoSetShow(None, fromList = showList)
            else:
                return Show.OneSetShow(None, fromList = showList)
        else:
            return -1

    def addShowToDatabase(self, show):
        date = show.getDate()
        self.c.execute('SELECT * FROM Shows WHERE Date = ?', [date])
        if self.c.fetchone() == None:
            venue = show.getVenue()
            location = show.getLocation()
            footer = show.getFooter()
            statement = "INSERT INTO Shows (date, venue, location, footer) VALUES (?, ?, ?, ?);"
            self.c.execute(statement, [date, venue, location, footer])

            setlist = show.getSetlist()
            for set in setlist:
                count = 0
                for song in setlist[set]:
                    songName = song.getTitle()
                    songDescription = song.getDescription()
                    statement = "INSERT INTO Songs (name, date, setName, songNumber, description) VALUES (?, ?, ?, ?, ?)"
                    self.c.execute(statement, [songName, date, set, count, songDescription])
                    count += 1
            self.conn.commit()

        else:
            return -1

    def addShowToUser(self, name, date):
        self.c.execute("SELECT * FROM Users WHERE name=? and date=?", [name, date])
        if self.c.fetchone() == None:
            self.c.execute("INSERT INTO Users (name, date) VALUES (?, ?)", [name, date])
            self.conn.commit()

    def removeShowFromUser(self, name, date):
        self.c.execute("SELECT * FROM Users WHERE name=? and date=?", [name, date])
        if self.c.fetchone() != None:
            self.c.execute("DELETE FROM Users WHERE name=? and date=?", [name, date])
            self.conn.commit()
