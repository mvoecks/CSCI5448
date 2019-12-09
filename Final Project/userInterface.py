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
