from Canine import Dog, Wolf
from Bird import Crow, Vulture
from Feline import Cat, Lion
from ZooKeeper import ZooKeeper
from ZooAnnouncer import ZooAnnoucer


import sys

''' The main function creates a list of animals, one Wof, dog, crow, vulture,
    cat, and lion. It then creates a ZooKeeper and passes it a the list of
    animals created. An ZooAnnoucer class is created and registered by the
    ZooKeeper. The ZooKeeper performs his responsibilities and then removes
    the observer from the subscriptions.
'''
def main():
    with open('..\\dayatthezoo.out', 'w') as f:
        sys.stdout = f

        animals = [Wolf('Wendy'), Dog('Doug'), Crow('Cathy'), Vulture('Vick'), Cat('Carl'), Lion('Leo')]
        keeper = ZooKeeper(animals)
        announcer = ZooAnnoucer()

        keeper.registerObserver(announcer)
        keeper.performResponsibilities()
        keeper.removeObserver(announcer)


if __name__ == '__main__':
    main()
