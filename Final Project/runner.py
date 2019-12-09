<<<<<<< HEAD
import userInterface as ui

# Get a user interface
interface = ui.userInterface()

# Log in the user
interface.login()

# While the user is logged in, keep giving them activities to choose from
loggedIn = True
while(loggedIn):
    loggedIn = interface.chooseActivity()
=======
import userInterface as ui

interface = ui.userInterface()
interface.login()
execute = True
while(execute):
    execute = interface.chooseActivity()
>>>>>>> 6dcc5a71e17c97d114ad61c655c55a7cd0ed138b
