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
    zooAnnouncement = ''

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
        animals, excercise the animals, and shut down the zoo. Using the
        functions defined below. Print statements are added to make the output
        text look nice.
    '''
    def performResponsibilities(self):
        self.wakeAnimals()
        print()
        self.rollCallAnimals()
        print()
        self.feedAnimals()
        print()
        self.excerciseAnimals()
        print()
        self.shutdownZoo()

    ''' Sets the zooAnnouncement, notifys the ZooKeeper's observers, prints a
        message to indicate he is waking the animals, then calls the wakeup
        function for each animal in animalList
    '''
    def wakeAnimals(self):
        zooAnnouncement = 'The ZooKeeper is about to wake the animals.'
        self.notifyObservers(zooAnnouncement)
        print("Zookeeper: I will now wake up the animals of the zoo.")
        for animal in self.animalList:
            animal.wakeup()

    ''' Sets the zooAnnouncement to indicate the roll call will begin, prints a
        message to indicate he is roll calling the animals, then calls the
        makeNoise function for each animal in animalList
    '''
    def rollCallAnimals(self):
        zooAnnouncement = 'Be ready to watch the ZooKeeper as he calls each animal for attendance.'
        self.notifyObservers(zooAnnouncement)
        print("Zookeeper: Animals! ROLL CALL!!!")
        for animal in self.animalList:
            animal.makeNoise()

    ''' Sets the zooAnnouncement to indicate the animals are about to be feed,
        prints a message saying he is about to feed the animals, then calls
        the eat function for each animal
    '''
    def feedAnimals(self):
        zooAnnouncement = 'It\'s feeding time for the animals, gather close to see them eat.'
        self.notifyObservers(zooAnnouncement)
        print("Zookeeper: Chow time. Dig in.")
        for animal in self.animalList:
            animal.eat()

    ''' Sets the zooAnnouncement to indicate the animals are about to roam,
        prints a message saying the animals can roam around, then calls the
        doRoam funciton for each animal.
    '''
    def excerciseAnimals(self):
        zooAnnouncement = 'It\'s time for the animals to roam around, watch to see their behavior.'
        self.notifyObservers(zooAnnouncement)
        print("Zookeeper: You're free to excercise now.")
        for animal in self.animalList:
            animal.doRoam()

    ''' Sets the zooAnnouncement to indicate the zoo will close soon, then
        prints a message saying each animal should go to bed, then calls the
        sleep function for each animal.
    '''
    def shutdownZoo(self):
        zooAnnouncement = 'We are closing down the zoo. Please head to the exits while we put the animals to sleep.'
        self.notifyObservers(zooAnnouncement)
        print("Zookeeper: Time for sleep, we're shutting down.")
        for animal in self.animalList:
            animal.sleep()
