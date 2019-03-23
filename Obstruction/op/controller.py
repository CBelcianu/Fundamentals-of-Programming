'''
Created on 30 dec. 2017

@author: Catalin
'''
class controller():
    def __init__(self,board):
        '''
        constructor for controller class
        input: board
        '''
        self.__board=board
    def movX(self,square):
        '''
        places a X in the given square
        input: square
        '''
        try:
            self.__board.moveX(square)
        except ValueError as ve:
            raise ValueError(ve)
    def movO(self,square):
        '''
        places a O in the given square
        input: square
        '''
        try:
            self.__board.moveO(square)
        except ValueError as ve:
            raise ValueError(ve)
    def getBoard(self):
        '''
        prints the board
        '''
        print(self.__board)
    def isGameWon(self):
        '''
        verifies if the game is won
        '''
        return self.__board.isGameWon()
    def findEmptySquare(self):
        '''
        finds an unoccupied square
        '''
        return self.__board.findEmptySquare()
    def clearBoard(self):
        '''
        clears the board
        '''
        self.__board.clear()
    def getC(self):
        return self.__board.getC()
    def getR(self):
        return self.__board.getR()