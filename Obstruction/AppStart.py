'''
Created on 30 dec. 2017

@author: Catalin
'''

from domain.components import board
from op.controller import controller
from ui.UI import UI
from utilities import readBoardSize

x,y=readBoardSize()
b=board(y,x)
ctr=controller(b)
ui=UI(ctr)

ui.main()