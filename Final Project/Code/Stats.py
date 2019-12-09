import abc
import heapq


''' Abstract Stat class: **STRAGETY PATTERN**
    Defines the name and collection for a statistic and has one abstract method,
    runStat(), which is the statistic code specified in subclasses to be run
    on the collection
'''
class Stat():
    __metaclass__ = abc.ABCMeta

    # Constructor, set name and collection
    def __init__(self, coll, name):
        self.collection = coll
        self.name = name

    # Get the name of the statistic
    def getName(self):
        return self.name

    # Abstract Method, defines the code for the statistic being run
    @abc.abstractmethod
    def runStat(self):
        return -1

''' top10StatClass (extends Stat):
    This class searches all the songs for each show in the collection and
    counts the number of times each song has been played. Then the heapq
    module is used to find which songs have been played most frequently, and
    the top 10 list of results is returned.
'''
class top10Stat(Stat):
    # Constructor
    def __init__(self, c):
        super().__init__(c, 'Top 10')

    def runStat(self):
        # Create a dictionary representing the list of songs and # of times played
        songCount = {}
        # Search each show in the collection and get each song from each show
        for show in self.collection:
            sl = self.collection[show].getSetlist()
            for set in sl:
                for song in sl[set]:
                    if song.getTitle() not in songCount:
                        songCount[song.getTitle()] = 1
                    else:
                        songCount[song.getTitle()] += 1

        # Use heapq to get the top 10 elements of the dictionary by songCount
        top10 = heapq.nlargest(10, songCount, key=songCount.get)
        top10List = []
        for song in top10:
            top10List.append((song, songCount[song]))

        # Format the return string so it looks nice.
        retString = '\n*****Top 10 Most Commonly Seen Songs*****\n'
        for song in top10List:
            retString += song[0]+": "+str(song[1])+'\n'
        return retString


''' bottom10Stat (extends Stat)
    This statistic gathers a songcount for each song in the users collection,
    and returns a string containing 10 songs they have seen the least
    frequently.
'''
class bottom10Stat(Stat):
    # Constructor
    def __init__(self, c):
        super().__init__(c, 'Bottom 10')

    def runStat(self):
        # Define a songcount dictionary
        songCount = {}
        # Loop through each show in the collection and extract song data
        for show in self.collection:
            sl = self.collection[show].getSetlist()
            for set in sl:
                for song in sl[set]:
                    if song.getTitle() not in songCount:
                        songCount[song.getTitle()] = 1
                    else:
                        songCount[song.getTitle()] += 1

        # Use heapq to get the 10 smallest elements in the dict by songcount
        bottom10 = heapq.nsmallest(10, songCount, key=songCount.get)
        bottom10List = []
        for song in bottom10:
            bottom10List.append((song, songCount[song]))

        # Format the return string in a nice way.
        retString = '\n*****Top 10 Least Seen Songs*****\n'
        for song in bottom10List:
            retString += song[0]+': '+str(song[1])+'\n'
        return retString

''' uniqueSongsSeen (extends Stat)
    This function searches through all songs in a users collection and creates
    a list of unique songs that they have seen. This list is then returned
'''
class uniqueSongsSeen(Stat):
    # Constructor
    def __init__(self, c):
        super().__init__(c, 'Unique Songs')

    def runStat(self):
        # Check if the user has any shows in their collection, and return if they dont
        if len(self.collection.keys()) == 0:
            return "\nUser has no shows in their collection.\n"
        else:
            # Create a list of unique songs
            songs = []
            # Loop through all songs in the collection
            for show in self.collection:
                sl = self.collection[show].getSetlist()
                for set in sl:
                    for song in sl[set]:
                        # Get teh title and add it to the list if it is unique
                        if song.getTitle() not in songs:
                            songs.append(song.getTitle())

            # Sort the list by alphabetical order
            songs.sort()

            # Format the return string in a nice way
            retString = '\n*****My Songs*****\n'
            for song in songs:
                retString += song+'\n'

            return retString

''' uniqueShowsSeen (extends Stat)
    This statistic just gets every show the user has seen and returns them to
    the user along with associated show info (venue and location).
'''
class uniqueShowsSeen(Stat):
    # Constructor
    def __init__(self, c):
        super().__init__(c, 'Unique Shows')

    def runStat(self):
        # Check if the user has any shows in their collection and return if they dont
        if len(self.collection.keys()) == 0:
            return "\nUser has no shows in their collection.\n"
        else:
            # Get the date, venue, and location of each show in the collection
            shows = '\n*****My Shows*****\n'
            for show in self.collection:
                shows += 'Date: '+str(show)+'\n'
                shows += 'Venue: '+str(self.collection[show].getVenue())+'\n'
                shows += 'Location: '+str(self.collection[show].getLocation())+'\n\n'

            return shows
