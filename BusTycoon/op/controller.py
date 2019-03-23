'''
Created on 19 dec. 2017

@author: Catalin
'''
from domain.entities import bus
from _operator import itemgetter
class controller():
    def __init__(self,repor,repob):
        self.__repor=repor
        self.__repob=repob
    def addRoute(self,route):
        self.__repor.add(route)
    def addBus(self,bus):
        self.__repob.add(bus)
    def commRoute(self,route):
        for b in self.__repob.getAll():
            if b.getRID()==route.getID():
                print(b)
    def incUsg(self,bID,rID):
        for b in self.__repob.getAll():
            if str(b.getBID())==str(bID) and str(b.getRID())==str(rID):
                b1=bus(b.getBID(),b.getRID(),b.getModel(),b.getTimes()+1)
                self.__repob.update(b,b1)
    def order(self):
        l=[]
        for b in self.__repob.getAll():
            for r in self.__repor.getAll():
                if r.getID()==b.getRID():
                    l.append([int(b.getBID()),int(b.getTimes())*int(r.getDist())])
        l=reversed(sorted(l,key=itemgetter(1)))
        for i in l:
            print(i)