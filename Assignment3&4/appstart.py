'''
Created on 6 nov. 2017

@author: Catalin
'''
from repository.numberRepo import NumberRepository
from operations.numberController import NumberController
from ui.menu import UI
from domain.complex import Complex


'''
    1. Initialize the repository
        - Repository holds the business entities
        - Acts like the program's database
        - Might include some data validation
        - Does not know about any other components
'''
repo = NumberRepository()

'''
    Add a few items to the repository
'''
repo.add(Complex(1, 2))
repo.add(Complex(4))
repo.add(Complex(0, -2))
repo.add(Complex(3, 6))
repo.add(Complex(14, -22))
repo.add(Complex(11, 20))
repo.add(Complex(3, -5))
repo.add(Complex(5, -2))
repo.add(Complex(6, 7))
repo.add(Complex(10, 2))
repo.add(Complex(7, -8))
repo.add(Complex(1, 2))

'''
    2. Initialize the controller
        - The controller implements the program's 'operations'
        - Knows only about the repository layer
        - 'Talks' to the repository and UI using parameter passing and expcetions
'''
controller = NumberController(repo)

'''
    3. Initialize the user interface
        - The UI implements all user interactions
        - Only knows about the controller layer
        - Calls functions from the controller to implement program features
        - Might include some data validation, as a fast-fail mechanism
'''
ui = UI(controller)

'''
    4. Start the application's user interface
'''
ui.mainMenu()