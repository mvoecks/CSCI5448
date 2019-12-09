import userInterface as ui

# Get a user interface
interface = ui.userInterface()

# Log in the user
interface.login()

# While the user is logged in, keep giving them activities to choose from
loggedIn = True
while(loggedIn):
    loggedIn = interface.chooseActivity()
