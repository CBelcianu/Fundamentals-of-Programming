'''
Created on 3 feb. 2018

@author: Catalin
'''
from domain.components import board
class boardfile(board):
    def __init__(self,fname="game.txt"):
        board.__init__(self)
        self.__fname=fname
        self.__load()
    def __load(self):
        f=open(self.__fname,"r")
        l=f.readline().strip
        while l!='':
            board.overrr(self,l)
            l=f.readline().strip
        f.close()
    def __store(self):
        f=open(self.__fname,"w")
        f.write(board.getData(self))
        f.close
    def movX(self,i,j):
        board.movX(self, i, j)
        self.__store()
    def movO(self,i,j):
        board.movO(self, i, j)
        self.__store()
    def replaceO(self, i, j, i1, j1):
        board.replaceO(self, i, j, i1, j1)
        self.__store()
    def replaceX(self, i, j, i1, j1):
        board.replaceX(self, i, j, i1, j1)
        self.__store()