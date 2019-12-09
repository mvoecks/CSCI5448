import requests
import re
from bs4 import BeautifulSoup
import abc

''' Creates a song that will be stored in a setlist for a show.
    Arguments include songData, a BeautifulSoup soup object
'''
class Song:
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

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description


class ShowFactory():
    def getShow(self, date):
        url = "https://api.phish.net/v3/setlists/get?apikey=54F48A9D48D56E6D1E97&showdate="+str(date)
        payload = "{}"
        response = requests.request("GET", url, data=payload)
        jsonResponse = response.json()

        if jsonResponse['response']['count'] == 0:
            return -1

        else:
            if 'Set 3' in jsonResponse['response']['data'][0]['setlistdata']:
                return ThreeSetShow(jsonResponse)

            elif 'Set 2' in jsonResponse['response']['data'][0]['setlistdata']:
                return TwoSetShow(jsonResponse)

            else:
                return OneSetShow(jsonResponse)

class Show():
    __metaclass__ = abc.ABCMeta

    def __init__(self, d, v, loc, sl, foot):
        self.date = d
        self.venue = v
        self.location = loc
        self.setlist = sl
        self.footer = foot

    def parseSetlist(self, setlistData):
        soup = BeautifulSoup(setlistData, features='html.parser')
        setlist = []
        footerInfo = []
        for tagMeta in soup.find_all("p"):
            setInfo = []
            for tag in tagMeta.contents:
                try:
                    if tag['class'] == ['setlist-song']:
                        setInfo.append(Song(tag))
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

    @abc.abstractmethod
    def printSetlist(self):
        print(self.setlist)

    def printStats(self):
        print(self.date)
        print(self.venue)
        print(self.location)
        self.printSetlist()

    def getSetlist(self):
        return self.setlist

    def getVenue(self):
        return self.venue

    def getLocation(self):
        return self.location

    def getDate(self):
        return self.date

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

class OneSetShow(Show):
    def __init__(self, apiData, fromList = None):
        if fromList == None:
            date = apiData['response']['data'][0]['showdate']
            venue = re.sub("<[^>]*>", "", apiData['response']['data'][0]['venue'])
            location = apiData['response']['data'][0]['location']
            setlist, footer = self.generateSetlist(apiData['response']['data'][0]['setlistdata'])
            super().__init__(date, venue, location, setlist, footer)
        else:
            super().__init__(fromList['date'], fromList['venue'], fromList['location'], fromList['setlist'], fromList['footer'])

    def generateSetlist(self, setlistData):
        setlistInfo, footerInfo = self.parseSetlist(setlistData)
        setlistDict = {}
        setlistDict['set1'] = setlistInfo[0]

        if (len(setlistInfo) == 1):
            setlistDict['encore'] = []
        else:
            setlistDict['encore'] = setlistInfo[1]

        return setlistDict, footerInfo

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
    def __init__(self, apiData, fromList = None):
        if fromList == None:
            date = apiData['response']['data'][0]['showdate']
            venue = re.sub("<[^>]*>", "", apiData['response']['data'][0]['venue'])
            location = apiData['response']['data'][0]['location']
            setlist, footer = self.generateSetlist(apiData['response']['data'][0]['setlistdata'])
            super().__init__(date, venue, location, setlist, footer)
        else:
            super().__init__(fromList['date'], fromList['venue'], fromList['location'], fromList['setlist'], fromList['footer'])

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
    def __init__(self, apiData, fromList = None):
        if fromList == None:
            date = apiData['response']['data'][0]['showdate']
            venue = re.sub("<[^>]*>", "", apiData['response']['data'][0]['venue'])
            location = apiData['response']['data'][0]['location']
            setlist, footer = self.generateSetlist(apiData['response']['data'][0]['setlistdata'])
            super().__init__(date, venue, location, setlist, footer)
        else:
            super().__init__(fromList['date'], fromList['venue'], fromList['location'], fromList['setlist'], fromList['footer'])


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
