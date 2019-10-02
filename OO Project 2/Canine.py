import abc
from Animal import Animal
from roamBehaviorAbstract import hunt

''' We will define the behavior of all Canines to hunt when they roaming,
    therefore we will create the roamBehaviorAbstract hunt class to use to
    set out roam behavior.
'''
huntBehavior = hunt()


''' Here we create our Canine abstract class. This is an extension of the animals
    class and defines the roam behavior and eating behavior of all canines and
    the sleep behavior for each Canine.
'''
class Canine(Animal):
    __metaclass__ = abc.ABCMeta

    ''' Initializing a Canine object and set its name, type, and behavior in
        the superclass Animal
    '''
    def __init__(self, name, type):
        super().__init__(name, type)
        super().setRoamBehavior(huntBehavior)

    ''' All Canines eat and sleep the same, so initialize these functions here
    '''
    def eat(self):
        print(super().getType() + "-" + super().getName() +": Bark Bark this is some good food.")

    def sleep(self):
        print(super().getType() + "-" + super().getName() +": Growl, time to sleep, Zzzzz.....")


''' Create a class for the dogs, which are an extension of Canines. In this
    class we initialize a dog by giving it a name. The only function defines how
    dogs will make noise.
'''
class Dog(Canine):
    def __init__(self, name):
        super().__init__(name, 'Dog')

    def makeNoise(self):
        print(super().getType() + "-" + super().getName() +": Woof Woof, I'm a dog.")


''' Create a class for the wolfs, which are an extension of Canines. In this
    class we initialize a wolfs by giving it a name. The only function defines how
    wolfs will make noise.
'''
class Wolf(Canine):
    def __init__(self, name):
        super().__init__(name, 'Wolf')

    def makeNoise(self):
        print(super().getType() + "-" + super().getName() +": Grrrrr, watch out I'm a wolf.")
