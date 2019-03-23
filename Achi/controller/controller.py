'''
Created on 3 feb. 2018

@author: Catalin
'''
#from domain.components import board
class controller():
    '''
    controller class
    '''
    def __init__(self,rep):
        '''
        constructor for controller class
        '''
        self.__rep=rep
    def movX(self,i,j):
        '''
        program that moves x to a square
        input:i,j
        '''
        self.__rep.movX(i,j)
    def movO(self,i,j):
        '''
        program that moves 0 to a square
        input:i,j
        '''
        self.__rep.movO(i,j)
    def printBoard(self):
        '''
        program that prints board
        '''
        return str(self.__rep)
    def fnd(self):
        '''
        program that finds an empty square
        '''
        self.__rep.findEmpty()
    def replaceX(self,i,j,i1,j1):
        '''
        program that moves x from one square to another
        '''
        try:
            self.__rep.replaceX(i,j,i1,j1)
        except ValueError as ve:
            raise ValueError(ve)
    #def replaceO(self):
        #self.__rep.replaceO()
    def mmmO(self):
        '''
        program that moves 0 from one square to another
        '''
        i,j=self.__rep.findO()
        i1,j1=self.__rep.findE()
        self.__rep.replaceO(i,j,i1,j1)
    def gw(self):
        '''
        program that verifies if the game is won
        '''
        return self.__rep.isgamewon()
    def datab(self):
        return self.__rep.getData()
    def dont(self):
        self.__rep.dont()
    

    