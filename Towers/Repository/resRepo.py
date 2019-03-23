'''
Created on 1 feb. 2018

@author: Catalin
'''
class occupiedRooms():
    def __init__(self):
        self.__data=[]
    def addRoom(self,r):
        self.__data.append(r)
    def removeRoom(self,nr):
        i=0
        while self.__data[i].getNr()!=nr:
            i+=1
        self.__data.pop(i)
    def getAll(self):
        return self.__data

class roomRepo():
    def __init__(self):
        self.__data=[]
    def addRoom(self,r):
        self.__data.append(r)
    def removeRoom(self,nr):
        i=0
        while self.__data[i].getNr()!=nr:
            i+=1
        self.__data.pop(i)
    def getAll(self):
        return self.__data

class resRepo():
    def __init__(self):
        self.__data=[]
    def addRes(self,r):
        self.__data.append(r)
    def removeRes(self,idd):
        i=0
        while self.__data[i].getID()!=idd:
            i+=1
        self.__data.pop(i)
    def getAll(self):
        return self.__data