from menu import Menu
from tesla import TeslaAPI

tesla = TeslaAPI()
success = tesla.initiate_communications()

if success:
    menu = Menu(tesla)
    menu.display(tesla, 'main')
