import abc
from Events import EventSubject


''' The ZooKeeper class extends the EventSubject abstract subject class. This
    class will register, remove, and notify observers and will maintain a list
    of animals that it will be in charge of. The ZooKeeper performs their
    responsibilities and notifies the observers when appropriate.
'''
class ZooKeeper(EventSubject):
    ''' Create two lists containing our observers and animals
    '''
    animalList = []
    eventObservers = []

    ''' Methods implimented from the EventSubject class, these will register,
        remove, and notify users in the eventObservers list.
    '''
    def registerObserver(self, observer):
        self.eventObservers.append(observer)

    def removeObserver(self, observer):
        self.eventObservers.remove(observer)

    def notifyObservers(self, eventText):
        for o in self.eventObservers:
            o.update(eventText)

    ''' The init function for the ZooKeeper assigns the animals he's in charge
        of at the moment.
    '''
    def __init__(self, animals):
        self.animalList = animals

    ''' A function to add animals if they are late to the party.
    '''
    def addAnimal(self, animal):
        self.animalList.append(animal)

    ''' This function will wake the animals, perform animal roll call, feed the
        animals, excercise the animals, and shut down the zoo. During each step
        we notify our observers about what we're doing, print the action we are
        about to do, and finally perform the actions, which are listed below.
    '''
    def performResponsibilities(self):
        self.notifyObservers('The ZooKeeper is about to wake the animals.')
        print("Zookeeper: I will now wake up the animals of the zoo.")
        self.wakeAnimals()

        self.notifyObservers('Be ready to watch the ZooKeeper as he calls each animal for attendance.')
        print("Zookeeper: Animals! ROLL CALL!!!")
        self.rollCallAnimals()

        self.notifyObservers('It\'s feeding time for the animals, gather close to see them eat.')
        print("Zookeeper: Chow time. Dig in.")
        self.feedAnimals()

        self.notifyObservers('It\'s time for the animals to roam around, watch to see their behavior.')
        print("Zookeeper: You're free to excercise now.")
        self.excerciseAnimals()

        self.notifyObservers('We are closing down the zoo. Please head to the exits while we put the animals to sleep.')
        print("Zookeeper: Time for sleep, we're shutting down.")
        self.shutdownZoo()

    ''' Calls the wakeup function for each animal in animalList
    '''
    def wakeAnimals(self):
        for animal in self.animalList:
            animal.wakeup()

    ''' Calls the makeNoise function for each animal in animalList
    '''
    def rollCallAnimals(self):
        for animal in self.animalList:
            animal.makeNoise()

    ''' Calls the eat function for each animal in animalList
    '''
    def feedAnimals(self):
        for animal in self.animalList:
            animal.eat()

    ''' Calls the doRoam function for each animal in animalList
    '''
    def excerciseAnimals(self):
        for animal in self.animalList:
            animal.doRoam()

    ''' Calls the sleep function for each animal in animalList
    '''
    def shutdownZoo(self):
        for animal in self.animalList:
            animal.sleep()
