import abc
from heapq import nlargest

class Stat():
    __metaclass__ = abc.ABCMeta

    def __init__(self, c):
        self.collection = c

    @abc.abstractmethod
    def runStat(self):
        return -1

class top10Stat(Stat):
    def __init__(self, c):
        super().__init__(c)

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

        top10 = nlargest(10, songCount, key=songCount.get)
        top10List = []
        for song in top10:
            top10List.append(song, songCount[song])
        return top10List
