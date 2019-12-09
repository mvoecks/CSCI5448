<<<<<<< HEAD
import User

''' The userInterface class contains the code related to displaying the current
    state of the program to the user via print statements.
'''
class userInterface:
    # Constructor
    def __init__(self):
        self.user = None

    ''' login function
        Gets the users username and creates a sets the user attribute for the
        interface by creating a new user with the username.
    '''
    def login(self):
        print("Welcome to My Phish Stats, please enter your username.")
        user = input()
        self.user = User.User(user)
        print("\nUser "+self.user.getName()+" successfully logged in. \n")

    ''' chooseActivity
        Prints a series of options which users can choose from, these are the
        main actions of the program.
    '''
    def chooseActivity(self):
        print("What would you like to do?")
        print("\t 1. Add a show to your collection")
        print("\t 2. Remove a show to your collection")
        print("\t 3. Check your show statistics")
        print("\t 4. View the setlist for a show.")
        print("\t 5. Loggout")
        print("**Please enter your choice as a number**")
        action = input()
        if action == '1':
            self.addShow()
        elif action == '2':
            self.removeShow()
        elif action == '3':
            self.printStat()
        elif action == '4':
            self.printSetlist()
        elif action == '5':
            print("\nThanks for using My Phish Stats\n")
            return False
        else:
            print("\nResponse not recognized, please try again. \n")
        return True


    ''' printSetlist function:
        Prompts the user for a show date and then searches their collection for
        the show's corrisponding setlist.
    '''
    def printSetlist(self):
        print("\nEnter the showdate you would like to view (YYYY-MM-DD):")
        showdate = input()
        show = self.user.getShow(showdate)
        if show == -1:
            # Show was not found in the collection, report to user
            print("\n Show not in users collection.\n")
        else:
            # Show found, print the setlist for the show.
            print("")
            show.printSetlist()
            print("")

    ''' addShow function:
        Prompts the user for a showdate that will be added to their collection
    '''
    def addShow(self):
        print("Enter the showdate you would like to add (YYYY-MM-DD):")
        showdate = input()
        response = self.user.addToCollection(showdate)
        if response == -1:
            # Show not found by the show creator factory
            print("\nThe requested date is not a valid show. \n")
        else:
            # Show found and added to the collection
            print("\nShow successfully added to your collection. \n")

    ''' removeShow function:
        Prompts the user for a showdate that will be removed from their collection
    '''
    def removeShow(self):
        print("Enter the showdate you would like to remove (YYYY-MM-DD):")
        showdate = input()
        response = self.user.removeFromCollection(showdate)
        if response == -1:
            # Show not found in the users collection
            print("\nThe requested showdate is currently not in your collection. \n")
        else:
            # Show found and removed from collection
            print("\nShow successfully removed from your collection. \n")

    ''' Prompts the user for which statistic they would like to run, and then
        prints the statistic of their choice.
    '''
    def printStat(self):
        print("\nChoose from the options below which statistic you would like to run:")
        print("\t 1. My Shows")
        print("\t 2. Unique Songs Seen")
        print("\t 3. Top 10 Most Commonly Seen Song")
        print("\t 4. Top 10 Least Seen Songs")

        # Get a list of all shows in the collection
        choice = input()
        if choice == '1':
            self.user.setStatistic('Unique Shows')
            shows = self.user.printStat()

        # Print all unique songs in the users collection
        elif choice == '2':
            self.user.setStatistic('Unique Songs')
            self.user.printStat()

        # Prints the user's top 10 most commonly seen songs
        elif choice == '3':
            self.user.setStatistic('Top 10')
            self.user.printStat()

        # Prints the user's top 10 least commonly seen songs
        elif choice == '4':
            self.user.setStatistic('Bottom 10')
            self.user.printStat()

        else:
            print("\nResponse not recognized, please try again.\n")
=======
import User

class userInterface:
    def __init__(self):
        self.user = None

    def login(self):
        print("Welcome to My Phish Stats, please enter your username.")
        user = input()
        self.user = User.User(user)
        print("\nUser "+self.user.getName()+" successfully logged in. \n")

    def chooseActivity(self):
        print("What would you like to do?")
        print("\t 1. Add a show to your collection")
        print("\t 2. Remove a show to your collection")
        print("\t 3. Check your show statistics")
        print("\t 4. Loggout")
        print("**Please enter your choice as a number**")
        action = input()
        if action == '1':
            self.addShow()
        elif action == '2':
            self.removeShow()
        elif action == '3':
            self.printStat()
        elif action == '4':
            print("\nThanks for using My Phish Stats\n")
            return False
        else:
            print("\nResponse not recognized, please try again. \n")
        return True

    def addShow(self):
        print("Enter the showdate you would like to add (YYYY-MM-DD).")
        showdate = input()
        response = self.user.addToCollection(showdate)
        if response == -1:
            print("\nThe requested date is not a valid show. \n")
        else:
            print("\nShow successfully added to your collection. \n")

    def removeShow(self):
        print("Enter the showdate you would like to remove (YYYY-MM-DD).")
        showdate = input()
        response = self.user.removeFromCollection(showdate)
        if response == -1:
            print("\nThe requested showdate is currently not in your collection. \n")
        else:
            print("\nShow successfully removed from your collection. \n")

    def printStat(self):
        print("\nChoose from the options below which statistic you would like to run:")
        print("\t 1. My Shows")
        print("\t 2. Unique Songs Seen")
        print("\t 3. Top 10 Most Commonly Seen Song")
        print("\t 4. Top 10 Least Seen Songs")

        choice = input()
        if choice == '1':
            self.user.setStatistic('Unique Shows')
            shows = self.user.printStat()

        elif choice == '2':
            self.user.setStatistic('Unique Songs')
            self.user.printStat()

        elif choice == '3':
            self.user.setStatistic('Top 10')
            self.user.printStat()

        elif choice == '4':
            self.user.setStatistic('Bottom 10')
            self.user.printStat()

        else:
            print("\nResponse not recognized, please try again.\n")
>>>>>>> 6dcc5a71e17c97d114ad61c655c55a7cd0ed138b
