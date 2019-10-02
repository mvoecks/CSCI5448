import abc
from Animal import Animal
from roamBehaviorAbstract import climbTree
from roamBehaviorAbstract import randomAction


''' The roaming behavior for Felines can either be to climb a tree or to do a
    random action. Therefore we create two roamBehaviorAbstract variables,
    climbTree and randomAction that we will set appropriately in the subclasses
    for Feline.
'''
climbBehavior = climbTree()
randomBehavior = randomAction()

''' Create a abstract class Feline which extends Animal. This class sets the
    doRoam behavior to the fly class, and impliments the eat and sleep functions
    defined in the abstract Animal class
'''
class Feline(Animal):
    __metaclass__ = abc.ABCMeta

    ''' Initializing a Feline object and set its name, type, and behavior in
        the superclass Animal
    '''
    def __init__(self, name, type, behavior):
        super().__init__(name, type)
        super().setRoamBehavior(behavior)

    ''' All Felines sleep and eat the same, so initialize those function Here
    '''
    def sleep(self):
        print(super().getType() + "-" + super().getName() +": Back to my natural state, Zzzzz.....")

    def eat(self):
        print(super().getType() + "-" + super().getName() +": Purrrr, some food. Don't mind if I do.")


''' Create a class for the cats, which are an extension of Felines. In this
    class we initialize a cat by giving it a name and defining its behavior,
    which is to do a random action. This also defines how cats make noise.
'''
class Cat(Feline):
    def __init__(self, name):
        super().__init__(name, 'Cat', randomBehavior)

    def makeNoise(self):
        print(super().getType() + "-" + super().getName() +": Meh, I'm just a cat.")


''' Create a class for the lions, which are an extension of Felines. In This
    class we initialize a lion by givig it a name and defining its behavior,
    which is to climb a tree. This also defines how lions make noise
'''
class Lion(Feline):
    def __init__(self, name):
        super().__init__(name, 'Lion', climbBehavior)

    def makeNoise(self):
        print(super().getType() + "-" + super().getName() +": ROAR! Behold the mighty lion!")
