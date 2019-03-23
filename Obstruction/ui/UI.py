'''
Created on 30 dec. 2017

@author: Catalin
'''
import time
from domain.components import square
class UI:
    def __init__(self,controller):
        '''
        constructor for UI class
        '''
        self.__controller=controller
    def main(self):
        '''
        the main program
        '''
        keepAlive=True
        playing=True
        while playing==True:
            self.__controller.clearBoard()
            self.__controller.getBoard()
            while keepAlive==True:
                ok=0
                while ok==0:
                    x,y=UI.readSquare()
                    x1,y1=x,y
                    try:
                        self.__controller.movX(square(x,y))
                        ok=1
                    except ValueError as ve:
                        print(ve)
                if self.__controller.isGameWon()==True:
                    self.__controller.getBoard()
                    print("you win")
                    break
                self.__controller.getBoard()
                x1=self.__controller.getC()+1-x1
                y1=self.__controller.getR()+1-y1
                print("thinking...")
                time.sleep(1)
                try:
                    self.__controller.movO(square(x1,y1))
                except ValueError:
                    x1,y1=self.__controller.findEmptySquare()
                    self.__controller.movO(square(x1,y1))
                if self.__controller.isGameWon()==True:
                    self.__controller.getBoard()
                    print("you loose")
                    break
                self.__controller.getBoard()
            playing=UI.continuePlaying()
        print("exit...")
    @staticmethod
    def readSquare():
        print("move at square:")
        x=int(input("x:"))
        y=int(input("y:"))
        return x,y
    @staticmethod
    def continuePlaying():
        print("do you want to start a new game? yes/no")
        x=1
        while x==1:
            x=input()
            if x=='yes':
                return True
            elif x=='no':
                return False
            else:
                print("invalid answer")
                x=1