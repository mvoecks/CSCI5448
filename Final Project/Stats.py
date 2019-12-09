import abc
import heapq

class Stat():
    __metaclass__ = abc.ABCMeta

    def __init__(self, coll, name):
        self.collection = coll
        self.name = name

    def getName(self):
        return self.name

    @abc.abstractmethod
    def runStat(self):
        return -1

class top10Stat(Stat):
    def __init__(self, c):
        super().__init__(c, 'Top 10')

    def runStat(self):
        songCount = {}
        for show in self.collection:
            sl = self.collection[show].getSetlist()
            for set in sl:
                for song in sl[set]:
                    if song.getTitle() not in songCount:
                        songCount[song.getTitle()] = 1
                    else:
                        songCount[song.getTitle()] += 1

        top10 = heapq.nlargest(10, songCount, key=songCount.get)
        top10List = []
        for song in top10:
            top10List.append((song, songCount[song]))

        retString = '\n*****Top 10 Most Commonly Seen Songs*****\n'
        for song in top10List:
            retString += song[0]+": "+str(song[1])+'\n'
        return retString


class bottom10Stat(Stat):
    def __init__(self, c):
        super().__init__(c, 'Bottom 10')

    def runStat(self):
        songCount = {}
        for show in self.collection:
            sl = self.collection[show].getSetlist()
            for set in sl:
                for song in sl[set]:
                    if song.getTitle() not in songCount:
                        songCount[song.getTitle()] = 1
                    else:
                        songCount[song.getTitle()] += 1

        bottom10 = heapq.nsmallest(10, songCount, key=songCount.get)
        bottom10List = []
        for song in bottom10:
            bottom10List.append((song, songCount[song]))

        retString = '\n*****Top 10 Least Seen Songs*****\n'
        for song in bottom10List:
            retString += song[0]+': '+str(song[1])+'\n'
        return retString


class uniqueSongsSeen(Stat):
    def __init__(self, c):
        super().__init__(c, 'Unique Songs')

    def runStat(self):
        if len(self.collection.keys()) == 0:
            return "\nUser has no shows in their collection.\n"
        else:
            songs = []
            for show in self.collection:
                sl = self.collection[show].getSetlist()
                for set in sl:
                    for song in sl[set]:
                        if song.getTitle() not in songs:
                            songs.append(song.getTitle())
            songs.sort()

            retString = '\n*****My Songs*****\n'
            for song in songs:
                retString += song+'\n'

            return retString

class uniqueShowsSeen(Stat):
    def __init__(self, c):
        super().__init__(c, 'Unique Shows')

    def runStat(self):
        if len(self.collection.keys()) == 0:
            return "\nUser has no shows in their collection.\n"
        else:
            shows = '\n*****My Shows*****\n'
            for show in self.collection:
                shows += 'Date: '+str(show)+'\n'
                shows += 'Venue: '+str(self.collection[show].getVenue())+'\n'
                shows += 'Location: '+str(self.collection[show].getLocation())+'\n\n'

            return shows
