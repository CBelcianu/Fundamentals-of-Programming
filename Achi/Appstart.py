'''
Created on 3 feb. 2018

@author: Catalin
'''
from domain.components import board
from controller.controller import controller
from ui.UI import UI
from gamefile import boardfile

b=board() #initialize a board
c=controller(b) #initialize a controller
u=UI(c) #initialize the user interface

u.main() #run the program