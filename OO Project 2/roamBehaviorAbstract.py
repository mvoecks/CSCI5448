import abc
import random

class roamBehaviorAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def roam(self):
        raise NotImplementedError


class fly(roamBehaviorAbstract):
    def roam(self):
        return "I'll take to the sky for some flying!"

class hunt(roamBehaviorAbstract):
    def roam(self):
        return "I'm going to hunt for some food for later."

class climbTree(roamBehaviorAbstract):
    def roam(self):
        return "This looks like a nice tree to climb, so lets climb it!"

class randomAction(roamBehaviorAbstract):
    def roam(self):
        randNumber = random.randint(0,4)
        if (randNumber == 0):
            return "I'll just go back to sleep, zzzzzzzz..."
        elif (randNumber == 1):
            return "Oh! I spotted a mouse I'll go chase."
        elif (randNumber == 2):
            return "Excercising is hard, can you just pet me instead?"
        elif (randNumber == 3):
            return "I can get my excercise by running on somebody's keyboard!"
        else:
            return "Don't tell me what to do."
