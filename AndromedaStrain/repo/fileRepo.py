'''
Created on 20 dec. 2017

@author: Catalin
'''
from repo.repo import personRepo
from domain.entities import person
class fileRepo(personRepo):
    def __init__(self,fileName="persons.txt"):
        personRepo.__init__(self)
        self.__fName=fileName
        self.__loadFromFile()
    def __loadFromFile(self):
        f=open(self.__fName,"r")
        line=f.readline().strip()
        while line!="":
            attrs=line.split(",")
            x=person(int(attrs[0]),attrs[1],attrs[2])
            personRepo.add(self,x)
            line=f.readline().strip()
        f.close()
            