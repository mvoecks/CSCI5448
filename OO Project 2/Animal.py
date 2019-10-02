import abc
from roamBehaviorAbstract import roamBehaviorAbstract

class Animal():
    __metaclass__ = abc.ABCMeta

    ''' Define variables for an animals name and type as well as appropriate
        getters and setters
    '''
    name = 'Unnamed'
    type = 'No Type'

    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName
    def getType(self):
        return self.type
    def setType(self, newType):
        self.type = newType


    ''' Define the initializing method that will create each Animal object.
        This will name and set the type of the Animal.
    '''
    def __init__(self, na, ty):
        self.setType(ty)
        self.setName(na)


    ''' Define a roamBehavior variable that will be set when initializing the
        animal with an appropriate setter. This is a part of a Stragety Pattern
        to seperate the roaming behavior of animals from the animals themselves.
    '''
    roamBehavior = roamBehaviorAbstract()

    def setRoamBehavior(self, newBehavior):
        self.roamBehavior = newBehavior


    ''' The roaming behavior of each animal varies, so here we will use The
        Stragety Pattern to offload the roam behavior to an abstract class
        roamBehaviorAbstract.py that has a abstract method roam(). Different
        classes are defined in that file on the specific roaming options that
        are available to animals
    '''
    @abc.abstractmethod
    def doRoam(self):
        print(self.getType() + "-" + self.getName() +": "+self.roamBehavior.roam())


    ''' Since all animals wake up the same, we can impliment the wakeup function
        here so subclasses don't have to impliment it
    '''
    def wakeup(self):
        print(self.getType() + "-" + self.getName() +": Yawn, I'm ready for a new day in the Zoo!")

    ''' The following methods are abstract methods that will be overriden by
        the animal subtype or the specific animal, they are required but not
        implemented here
    '''
    @abc.abstractmethod
    def makeNoise(self):
        raise NotImplementedError

    @abc.abstractmethod
    def eat(self):
        raise NotImplementedError

    @abc.abstractmethod
    def sleep(self):
        raise NotImplementedError
