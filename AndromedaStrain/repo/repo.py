'''
Created on 20 dec. 2017

@author: Catalin
'''
class personRepo():
    def __init__(self):
        self.__data=[]
    def getAll(self):
        return self.__data
    def update(self,p,p1):
        for i in range(0,len(self.__data)):
            if str(self.__data[i])==str(p):
                self.__data[i]=p1
    def add(self,x):
        self.__data.append(x)