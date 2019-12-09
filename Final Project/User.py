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
