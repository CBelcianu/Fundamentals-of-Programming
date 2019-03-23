'''
Created on 19 dec. 2017

@author: Catalin
'''
from domain.entities import route
class UI:
    def __init__(self,controller):
        self.__controller=controller
    def printMenu(self):
        print("\t 1. display all the buses traveling on a certain route")
        print("\t 2. inc usage")
        print("\t 3.list buses sorted by ditance travelled")
    def main(self):
        flg=True
        while flg==True:
            self.printMenu()
            cmd=input(">>").strip()
            if cmd=='1':
                r=UI.readRoute()
                self.__controller.commRoute(r)
            elif cmd=='2':
                bID,rID=UI.readIDS()
                self.__controller.incUsg(bID,rID)
            elif cmd=='3':
                self.__controller.order()
                
    @staticmethod
    def readRoute():
        id=int(input("id:"))
        dist=int(input("lenght:"))
        return route(id,dist)
    @staticmethod
    def readIDS():
        bID=input("bus:")
        rID=input("route:")
        return bID,rID