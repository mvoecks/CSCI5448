import sqlite3
import Show

''' Database class:
    Establishes a connection with the local sqlite3 database and is the bridge
    between a users actions and updates and queries to the database.

    This implements the facade pattern to make interfacing with the Database
    easier for the main program.
'''
class Database():
    ''' Constructor
        connects to the database specified by dbName, and creates the connection
        and cursor local variables
    '''
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName)
        self.c = self.conn.cursor()

    ''' del function:
        Closes the connection with the database when the database object is deleted
    '''
    def __del__(self):
        self.conn.close()

    ''' loadUser function:
        Checks the database to see if a user has any shows already added to his
        collection. If he doesnt exist in the database -1 is returned, otherwise
        a list of the shows in his collection is returned.
    '''
    def loadUser(self, name):
        # Search the database for the user
        self.c.execute('SELECT * FROM Users WHERE name = ?', [name])
        shows = self.c.fetchall()
        if shows == []:
            # User not in database, return -1
            return -1
        else:
            # User in database, parse the list of his shows and return them
            showlist = []
            for date in shows:
                showlist.append(date[1])
            return showlist

    ''' inDatabase function:
        Queries the database to see if a show exists in the database. Returns
        a boolean that is True if it is in the database, false otherwise
    '''
    def inDatabase(self, date):
        self.c.execute('SELECT * FROM Shows WHERE Date = ?', [date])
        if self.c.fetchone() == None:
            return False
        else:
            return True

    ''' getShowFromDatabase function:
        Queries the database for a specific show and creates a show object
        if there is a result in the database.
    '''
    def getShowFromDatabase(self, date):
        # Search for the show specified by date
        self.c.execute('SELECT * FROM Shows WHERE Date = ?', [date])
        showInfo = self.c.fetchone()
        if showInfo != None:
            # Show exists in the database, now we parse its info.
            # Get the date, venue, location, and footer directly
            showList = {}
            showList['date'] = showInfo[0]
            showList['venue'] = showInfo[1]
            showList['location'] = showInfo[2]
            showList['footer'] = showInfo[3].split(',')

            # Search the song database for the songs associated with this show
            self.c.execute('SELECT * FROM Songs WHERE Date=? ORDER BY setName, songNumber', [date])
            songInfo = self.c.fetchall()
            setlist = {}
            # Parse each set in the setlist
            for song in songInfo:
                # Create a setlist dictionary of songs
                tempSong = Show.Song(song[0], songDesc = song[4])
                if song[2] in setlist:
                    setlist[song[2]].append(tempSong)
                else:
                    setlist[song[2]] = [tempSong]
            showList['setlist'] = setlist

            # Determine what type of show to create and return it with correct parameters
            if 'set3' in setlist:
                return Show.ThreeSetShow(None, fromList = showList)
            elif 'set2' in setlist:
                return Show.TwoSetShow(None, fromList = showList)
            else:
                return Show.OneSetShow(None, fromList = showList)
        else:
            # Show not found, return -1 to indicate so
            return -1


    ''' addShowToDatabase function:
        This function accepts a show as an argument and enters its data into them
        database for quick reference in the future
    '''
    def addShowToDatabase(self, show):
        # Get the date of the show and check if its already in the database
        date = show.getDate()
        self.c.execute('SELECT * FROM Shows WHERE Date = ?', [date])
        if self.c.fetchone() == None:
            # Show not in the database, parse its data and add it
            # Get the venue, location, and notes and add it to the Show table
            venue = show.getVenue()
            location = show.getLocation()
            footer = show.getFooter()
            statement = "INSERT INTO Shows (date, venue, location, footer) VALUES (?, ?, ?, ?);"
            self.c.execute(statement, [date, venue, location, footer])

            # Parse through the songs of the setlist and add them to the song table
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
            # Show already in the database, do nothing.
            return -1

    ''' Creates an entry in the User table corrisponding to the users name
        and the show they have added to their collection
    '''
    def addShowToUser(self, name, date):
        # Test to see if this user already has this show
        self.c.execute("SELECT * FROM Users WHERE name=? and date=?", [name, date])
        if self.c.fetchone() == None:
            # Show not in collection, so lets add it
            self.c.execute("INSERT INTO Users (name, date) VALUES (?, ?)", [name, date])
            self.conn.commit()

    ''' Removes an entry from the User table corrisponding to the users name
        and the show they want to remove
    '''
    def removeShowFromUser(self, name, date):
        # Test to see if this uses even has the show they want to remove
        self.c.execute("SELECT * FROM Users WHERE name=? and date=?", [name, date])
        if self.c.fetchone() != None:
            # User has the show, lets remove it from their collection
            self.c.execute("DELETE FROM Users WHERE name=? and date=?", [name, date])
            self.conn.commit()
