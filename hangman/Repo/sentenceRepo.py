'''
Created on 31 ian. 2018

@author: Catalin
'''
from random import randint
class sentenceRepo():
    def __init__(self):
        self.__data=[]
    def addSentence(self,s):
        self.__data.append(s)
    def getAll(self):
        return self.__data
    def find(self,s):
        for i in self.__data:
            if i.lower()==s.lower():
                return False
        return True
    def randomSentence(self):
        x=randint(0,len(self.__data)-1)
        return self.__data[x]