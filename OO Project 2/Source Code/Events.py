import abc

''' Event subjects will be in charge of storing and managing event observers,
    and notify them when their notifyObservers method is called. This is an
    abstract class.
'''
class EventSubject():
    __metaclass__ = abc.ABCMeta

    ''' Register an observer to your subscription list.
    '''
    @abc.abstractmethod
    def registerObserver(self, observer):
        raise NotImplementedError

    ''' Remove an observer from your subscription lists.
    '''
    @abc.abstractmethod
    def removeObserver(self, observer):
        raise NotImplementedError

    ''' Go through your list of observers and call their update function
        appropriately.
    '''
    @abc.abstractmethod
    def notifyObservers(self):
        raise NotImplementedError

''' The event observer class is an abstract class that looks for information
    from EventSubjects, and updates itself appropriatly.
'''
class EventObserver():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, eventText):
        raise NotImplementedError
