import requests
import re
from bs4 import BeautifulSoup
import abc

''' Creates a song that will be stored in a setlist for a show.
    Arguments include songData, a BeautifulSoup soup object
'''
class Song:
    # Constructor, sets the title and song description
    def __init__(self, songData, songDesc = None):
        if songDesc == None:
            self.title = str(songData.string)
            try:
                self.description = str(songData['title'])
            except KeyError:
                self.description = ''
        else:
            self.title = songData
            self.description = songDesc

    # return the title of the song
    def getTitle(self):
        return self.title

    # returns the description of the song
    def getDescription(self):
        return self.description

''' FACTORY DESIGN PATTERN
    Allows users to create a show factory that searches the Phish.net API for
    shows to add to users collection.
'''
class ShowFactory():
    ''' getShow function:
        searches the phish.net for the showdate specified in the arguments.
        If no show is found a -1 error is returned. Otherwise it will return
        a Show object.
    '''
    def getShow(self, date):
        # Contact the API and get the showdate requested
        url = "https://api.phish.net/v3/setlists/get?apikey=54F48A9D48D56E6D1E97&showdate="+str(date)
        payload = "{}"
        response = requests.request("GET", url, data=payload)
        jsonResponse = response.json()

        # If no show was found, return an error
        if jsonResponse['response']['count'] == 0:
            return -1

        else:
            # Test the results to see what type of show needs to be created
            if 'Set 3' in jsonResponse['response']['data'][0]['setlistdata']:
                return ThreeSetShow(jsonResponse)
            elif 'Set 2' in jsonResponse['response']['data'][0]['setlistdata']:
                return TwoSetShow(jsonResponse)
            else:
                return OneSetShow(jsonResponse)

''' Show Abstract Class
    Defines the date, venue, location, setlist, and show notes for a given show.
    Includes basic getters and a function to parse the json objects for their
    setlist data. Has one abstract method for how to print the setlist
'''
class Show():
    __metaclass__ = abc.ABCMeta

    # Constructor, sets date, venue, location, setlist, and show notes
    def __init__(self, d, v, loc, sl, foot):
        self.date = d
        self.venue = v
        self.location = loc
        self.setlist = sl
        self.footer = foot

    ''' Parse setlist function:
        This function accepts the JSON data from a phish.net api request and
        extracts the setlist data for the show in a usable form
    '''
    def parseSetlist(self, setlistData):
        # Create a BeautifulSoup object to parse the data
        soup = BeautifulSoup(setlistData, features='html.parser')
        # Create a list for songs and for the show notes
        setlist = []
        footerInfo = []
        # Search each set
        for tagMeta in soup.find_all("p"):
            setInfo = []
            # Search all tags in the set
            for tag in tagMeta.contents:
                try:
                    # Find all tags that corrispond to a song in the set
                    if tag['class'] == ['setlist-song']:
                        setInfo.append(Song(tag))
                    # Find all tags that corrispond to a show note
                    elif tag['class'] == ['setlist-footer']:
                        for subTag in tag.contents:
                            if str(type(subTag)) != "<class 'bs4.element.Tag'>":
                                footerInfo.append(str(subTag))
                except TypeError:
                    pass
                except KeyError:
                    pass
            if len(setInfo) > 0:
                setlist.append(setInfo)
        return setlist, footerInfo

    # Abstract methods: Defines how a show should print its setlist
    @abc.abstractmethod
    def printSetlist(self):
        print(self.setlist)

    # Returns the setlist for the show
    def getSetlist(self):
        return self.setlist

    # Returns the venue for the show
    def getVenue(self):
        return self.venue

    # Returns the location of the show
    def getLocation(self):
        return self.location

    # Returns the date the show was played
    def getDate(self):
        return self.date

    # Returns the notes for the show
    def getFooter(self):
        if len(self.footer) == 0:
            return ''
        else:
            retString = ''
            for note in self.footer:
                retString += note
                retString += ', '
            retString = retString[:-2]
            return retString

''' OneSetShow
    Defines how a show with one set should be created and how to print its setlist
'''
class OneSetShow(Show):
    ''' Constructor, if the show was in the database it will be added directly,
        otherwise it parses the JSON data returned by the API request
    '''
    def __init__(self, apiData, fromList = None):
        if fromList == None:
            # Import the show from api data given in JSON form
            date = apiData['response']['data'][0]['showdate']
            venue = re.sub("<[^>]*>", "", apiData['response']['data'][0]['venue'])
            location = apiData['response']['data'][0]['location']
            setlist, footer = self.generateSetlist(apiData['response']['data'][0]['setlistdata'])
            super().__init__(date, venue, location, setlist, footer)
        else:
            # Import the show from data queried from the database
            super().__init__(fromList['date'], fromList['venue'], fromList['location'], fromList['setlist'], fromList['footer'])

    ''' generateSetlist function:
        Takes the setlist data extracted from the API request and converts it
        to a dictionary that is more easily read.
    '''
    def generateSetlist(self, setlistData):
        setlistInfo, footerInfo = self.parseSetlist(setlistData)
        setlistDict = {}
        setlistDict['set1'] = setlistInfo[0]

        if (len(setlistInfo) == 1):
            setlistDict['encore'] = []
        else:
            setlistDict['encore'] = setlistInfo[1]

        return setlistDict, footerInfo

    # Defines how the setlist of a one set show should be displayed.
    def printSetlist(self):
        print("Set 1:")
        for song in self.setlist['set1']:
            print(song.getTitle())
        print("Encore:")
        for song in self.setlist['encore']:
            print(song.getTitle())
        print("Notes:")
        for song in self.footer:
            print(song)

class TwoSetShow(Show):
    ''' Constructor, if the show was in the database it will be added directly,
        otherwise it parses the JSON data returned by the API request
    '''
    def __init__(self, apiData, fromList = None):
        if fromList == None:
            date = apiData['response']['data'][0]['showdate']
            venue = re.sub("<[^>]*>", "", apiData['response']['data'][0]['venue'])
            location = apiData['response']['data'][0]['location']
            setlist, footer = self.generateSetlist(apiData['response']['data'][0]['setlistdata'])
            super().__init__(date, venue, location, setlist, footer)
        else:
            super().__init__(fromList['date'], fromList['venue'], fromList['location'], fromList['setlist'], fromList['footer'])

    ''' generateSetlist function:
        Takes the setlist data extracted from the API request and converts it
        to a dictionary that is more easily read.
    '''
    def generateSetlist(self, setlistData):
        setlistInfo, footerInfo = self.parseSetlist(setlistData)
        setlistDict = {}
        setlistDict['set1'] = setlistInfo[0]
        setlistDict['set2'] = setlistInfo[1]

        if (len(setlistInfo) == 2):
            setlistDict['encore'] = []
        else:
            setlistDict['encore'] = setlistInfo[2]

        return setlistDict, footerInfo

    # Defines how the setlist of a two set show should be displayed.
    def printSetlist(self):
        print("Set 1:")
        for song in self.setlist['set1']:
            print(song.getTitle())
        print("Set 2:")
        for song in self.setlist['set2']:
            print(song.getTitle())
        print("Encore:")
        for song in self.setlist['encore']:
            print(song.getTitle())
        print("Notes:")
        for song in self.footer:
            print(song)

class ThreeSetShow(Show):
    ''' Constructor, if the show was in the database it will be added directly,
        otherwise it parses the JSON data returned by the API request
    '''
    def __init__(self, apiData, fromList = None):
        if fromList == None:
            date = apiData['response']['data'][0]['showdate']
            venue = re.sub("<[^>]*>", "", apiData['response']['data'][0]['venue'])
            location = apiData['response']['data'][0]['location']
            setlist, footer = self.generateSetlist(apiData['response']['data'][0]['setlistdata'])
            super().__init__(date, venue, location, setlist, footer)
        else:
            super().__init__(fromList['date'], fromList['venue'], fromList['location'], fromList['setlist'], fromList['footer'])

    ''' generateSetlist function:
        Takes the setlist data extracted from the API request and converts it
        to a dictionary that is more easily read.
    '''
    def generateSetlist(self, setlistData):
        setlistInfo, footerInfo = self.parseSetlist(setlistData)
        setlistDict = {}
        setlistDict['set1'] = setlistInfo[0]
        setlistDict['set2'] = setlistInfo[1]
        setlistDict['set3'] = setlistInfo[2]

        # No Encore, skip, set to ''
        if (len(setlistInfo) == 1):
            setlistDict['encore'] = []
        else:
            setlistDict['encore'] = setlistInfo[3]

        return setlistDict, footerInfo

    # Defines how the setlist of a two set show should be displayed.
    def printSetlist(self):
        print("Set 1:")
        for song in self.setlist['set1']:
            print(song.getTitle())
        print("Set 2:")
        for song in self.setlist['set2']:
            print(song.getTitle())
        print("Set 3:")
        for song in self.setlist['set3']:
            print(song.getTitle())
        print("Encore:")
        for song in self.setlist['encore']:
            print(song.getTitle())
        print("Notes:")
        for song in self.footer:
            print(song)
