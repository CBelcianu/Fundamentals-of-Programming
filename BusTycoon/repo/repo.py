'''
Created on 19 dec. 2017

@author: Catalin
'''
class routeRepo():
    def __init__(self):
        self.__data=[]
    def add(self,route):
        self.__data.append(route)
    def getAll(self):
        return self.__data
    
class busRepo():
    def __init__(self):
        self.__data=[]
    def add(self,bus):
        self.__data.append(bus)
    def getAll(self):
        return self.__data
    def update(self,b,b1):
        for i in range(0,len(self.__data)):
            if str(self.__data[i])==str(b):
                self.__data[i]=b1