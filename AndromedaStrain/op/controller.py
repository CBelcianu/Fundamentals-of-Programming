'''
Created on 20 dec. 2017

@author: Catalin
'''
from repo.repo import personRepo
from domain.entities import person
class controller:
    def __init__(self,repo):
        self.__repo=repo
    def simulate(self):
        '''
        simulates a day
        '''
        k=0
        ok=0
        for p1 in self.__repo.getAll():
            if p1.getStatus()=="ill":
                ok=1
        if ok==1:
            for p in self.__repo.getAll():
                if p.getImm()=="nonvaccinated" and p.getStatus()=="healthy":
                    p1=person(int(p.getID()),p.getImm(),"ill")
                    self.__repo.update(p,p1)
                    k=1
                    break
            if k==0:
                raise ValueError("no healthy person left")
        else:
            raise ValueError("no ill person left!")
    def all(self):
        '''
        returns a list of all persons
        '''
        return self.__repo.getAll()
    def vaccinate(self,p):
        '''
        vaccinates a healthy person
        '''
        k=0
        for i in self.__repo.getAll():
            if str(p)==str(i.getID()) and i.getStatus()=="healthy":
                p1=person(int(i.getID()),"vaccinated",i.getStatus())
                self.__repo.update(i,p1)
                k=1
        if k==0: 
            raise ValueError("person is not healthy")
    def update(self,p,p1):
        '''
        udates a person
        '''
        for i in self.__repo.getAll():
            if str(i)==str(p):
                self.__repo.update(p,p1)
                
def tests():
    '''
    runs tests for the controller class
    '''
    l=personRepo()
    l.add(person(1,"nonvaccindated","healthy"))
    l.add(person(2,"nonvaccindated","ill"))
    l.add(person(3,"nonvaccindated","healthy"))
    x=controller(l)
    x.vaccinate(3)
    assert str(l.getAll()[2])==str(person(3,"vaccinated","healthy"))
    x.update(person(2,"nonvaccindated","ill"),person(2,"vaccinated","ill"))
    assert str(l.getAll()[1])==str(person(2,"vaccinated","ill"))
tests()