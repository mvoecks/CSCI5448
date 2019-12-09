<<<<<<< HEAD
import Show
import Database
import Stats

''' User class:
    Manages a users show collection and allows the user to set the setStatistic
    they want and print it to the screen.
'''
class User:

    ''' Constructor
        Creates an empty collection, sets the users name, defines a ShowFactory
        and a database connection, and finally loads users shows if they are
        in the database
    '''
    def __init__(self, n):
        self.myCollection = {}
        self.name = n
        self.currentStat = None
        self.creator = Show.ShowFactory()
        self.database = Database.Database('phishstats')
        self.loadUserFromDatabase()

    # Returns the name of the user
    def getName(self):
        return self.name

    # Returns a show specified if its in the users collection
    def getShow(self, date):
        if date in self.myCollection:
            return self.myCollection[date]
        else:
            return -1

    # Searches for the user in the database, loads his shows if he is in there
    def loadUserFromDatabase(self):
        showsToLoad = self.database.loadUser(self.name)
        if showsToLoad != -1:
            for show in showsToLoad:
                self.addToCollection(show)

    def __del__(self):
        del self.database

    ''' Adds a show to a users collection
        If the show is in the database, it will load from there instead of
        checking the API. Otherwise calls the creators getShow(date) function
        to get the show and adds it to the database and the users collection
    '''
    def addToCollection(self, date):
        # Check if the show exists in the database
        if self.database.inDatabase(date) == True:
            show = self.database.getShowFromDatabase(date)
            self.myCollection[date] = show
            self.database.addShowToUser(self.name, date)
            return 0
        else:
            # Get the show from the show creator
            show = self.creator.getShow(date)
            if show == -1:
                # There was a problem getting the show, return -1 error
                return -1
            else:
                # Show was found, add it to the collection and to the database
                self.myCollection[date] = show
                self.database.addShowToDatabase(show)
                self.database.addShowToUser(self.name, date)
                return 0

    ''' Remove a show from your collection and from the users database profile
    '''
    def removeFromCollection(self, date):
        if date in self.myCollection.keys():
            del self.myCollection[date]
            self.database.removeShowFromUser(self.name, date)
            return 0
        else:
            return -1

    # Set the current statistics that will be printed to the page
    def setStatistic(self, s):
        if s == 'Top 10':
            self.currentStat = Stats.top10Stat(self.myCollection)
        if s == 'Bottom 10':
            self.currentStat = Stats.bottom10Stat(self.myCollection)
        if s == 'Unique Songs':
            self.currentStat = Stats.uniqueSongsSeen(self.myCollection)
        if s == 'Unique Shows':
            self.currentStat = Stats.uniqueShowsSeen(self.myCollection)

    # Run and print the statistic that is currently set.
    def printStat(self):
        print(self.currentStat.runStat())
=======
import Show
import Database
import Stats

class User:

    def __init__(self, n):
        self.myCollection = {}
        self.name = n
        self.setStatistic('Top 10')
        self.creator = Show.ShowFactory()
        self.database = Database.Database('phishstats')
        self.loadUserFromDatabase()

    def getName(self):
        return self.name

    def loadUserFromDatabase(self):
        showsToLoad = self.database.loadUser(self.name)
        if showsToLoad != -1:
            for show in showsToLoad:
                self.addToCollection(show)

    def __del__(self):
        del self.database

    def addToCollection(self, date):
        if self.database.inDatabase(date) == True:
            show = self.database.getShowFromDatabase(date)
            self.myCollection[date] = show
            self.database.addShowToUser(self.name, date)
            return 0
        else:
            show = self.creator.getShow(date)
            if show == -1:
                return -1
            else:
                self.myCollection[date] = show
                self.database.addShowToDatabase(show)
                self.database.addShowToUser(self.name, date)
                return 0

    def removeFromCollection(self, date):
        if date in self.myCollection.keys():
            del self.myCollection[date]
            self.database.removeShowFromUser(self.name, date)
            return 0
        else:
            return -1

    def setStatistic(self, s):
        if s == 'Top 10':
            self.currentStat = Stats.top10Stat(self.myCollection)
        if s == 'Bottom 10':
            self.currentStat = Stats.bottom10Stat(self.myCollection)
        if s == 'Unique Songs':
            self.currentStat = Stats.uniqueSongsSeen(self.myCollection)
        if s == 'Unique Shows':
            self.currentStat = Stats.uniqueShowsSeen(self.myCollection)

    def printStat(self):
        print(self.currentStat.runStat())
>>>>>>> 6dcc5a71e17c97d114ad61c655c55a7cd0ed138b
