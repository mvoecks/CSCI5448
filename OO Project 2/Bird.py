import abc
from Animal import Animal
from roamBehaviorAbstract import fly

''' The roaming behavior for birds is for them to fly, so we will create the
    roamBehaviorAbstract fly class to be used later when setting the roam
    behavior
'''
flyBehavior = fly()

''' Create a abstract class Bird which extends Animal. This class sets the
    doRoam behavior to the fly class and defines how each Bird sleeps
'''
class Bird(Animal):
    __metaclass__ = abc.ABCMeta

    ''' Initializing a Bird object and set its name, type, and behavior in
        the superclass Animal
    '''
    def __init__(self, name, type):
        super().__init__(name, type)
        super().setRoamBehavior(flyBehavior)

    ''' All Birds sleep the same, so initialize the sleep function Here
    '''
    def sleep(self):
        print(super().getType() + "-" + super().getName() +": Flying is exausting, Zzzzz.....")


''' Create a class for the crows, which are an extension of Birds. In this
    class we initialize a crow by giving it a name. Crows have two specific
    functions, makeNoise which defines how crows will make noise, and eat which
    defines how crows eat
'''
class Crow(Bird):
    def __init__(self, name):
        super().__init__(name, 'Crow')

    def makeNoise(self):
        print(super().getType() + "-" + super().getName() +": Caw! Caw! Look at this crow!")

    def eat(self):
        print(super().getType() + "-" + super().getName() +": Peck, Peck. Mmmmmm, delicious seeds")


''' Create a class for the vultures, which are an extension of Birds. In this
    class we initialize a vulture by giving it a name. Vultures have two
    specific functions, makeNoise which defines how vultures will make noise, and
    eat which defines how vultures eat
'''
class Vulture(Bird):
    def __init__(self, name):
        super().__init__(name, 'Vulture')

    def makeNoise(self):
        print(super().getType() + "-" + super().getName() +": Rasp, hisss. Don't talk to me.")

    def eat(self):
        print(super().getType() + "-" + super().getName() +": Rip! Yank! One man's trash....")
