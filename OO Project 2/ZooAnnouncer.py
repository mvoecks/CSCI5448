import abc
from Events import EventObserver

''' The ZooAnnoucer class extends the EventObserver and has a simple update
    function which accepts an eventText and then prints it.
'''
class ZooAnnoucer(EventObserver):
    def update(self, eventText):
        print('Announcer: '+eventText)
