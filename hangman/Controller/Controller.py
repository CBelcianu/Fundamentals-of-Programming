'''
Created on 31 ian. 2018

@author: Catalin
'''
class Controller():
    def __init__(self,repo):
        self.__repo=repo
    def addSentence(self,s):
        self.__repo.addSentence(s)
    def getAll(self):
        return self.__repo.getAll()
    def find(self,s):
        return self.__repo.find(s)
    def randomSentence(self):
        return self.__repo.randomSentence()