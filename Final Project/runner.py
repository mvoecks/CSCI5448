import userInterface as ui

interface = ui.userInterface()
interface.login()
execute = True
while(execute):
    execute = interface.chooseActivity()
