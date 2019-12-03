import Show
import Database
import Stats

class User:

    def __init__(self, n):
        self.myCollection = {}
        self.name = n
        self.currentStat = None
        self.creator = Show.ShowFactory()
        self.database = Database.Database('phishstats')

    def __del__(self):
        del self.database

    def addToCollection(self, date):
        if self.database.inDatabase(date) == True:
            show = self.database.getShowFromDatabase(date)
            self.myCollection[date] = show
        else:
            show = self.creator.getShow(date)
            if show == -1:
                print("Show not found, please try again.")
            else:
                self.myCollection[date] = show
                self.database.addShowToDatabase(show)

    def removeFromCollection(self, date):
        if date in self.myCollection.keys():
            del self.myCollection[date]

    def setStatistic(self, s):
        if s == 'Top 10':
            self.currentStat = Stats.top10Stat(self.myCollection)

    def printStat(self):
        print(self.currentStat.runStat())

    def printShows(self):
        for date in self.myCollection:
            print("Date: "+date)
            print("Venue: "+self.myCollection[date].getVenue())
            print("Location: "+self.myCollection[date].getLocation())
            print("Footer: "+self.myCollection[date].getFooter())
            print("")
