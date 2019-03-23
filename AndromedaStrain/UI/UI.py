'''
Created on 20 dec. 2017

@author: Catalin
'''
from domain.entities import person
class ui:
    def __init__(self,ctrl):
        self.__ctrl=ctrl
    def printMenu(self):
        print("\t 1.simulate day")
        print("\t 2.list all")
        print("\t 3.vaccinate a person")
    def main(self):
        flg=True
        k=0
        l=self.__ctrl.all()
        while flg==True:
            self.printMenu()
            cmd=input("Enter command:").strip()
            if cmd=='1':
                try:
                    self.__ctrl.simulate()
                    k=k+1
                    if k%3==0:
                        r=self.__ctrl.all()
                        for i in range(0,len(r)):
                            if str(l[i])==str(r[i]) and l[i].getStatus()=='ill':
                                self.__ctrl.update(l[i],person(int(l[i].getID()),l[i].getImm(),'healthy'))
                                l=self.__ctrl.all()
                except ValueError as ve:
                    print(ve)
            elif cmd=='2':
                l=self.__ctrl.all()
                for i in l:
                    print(i)
            elif cmd=='3':
                p=ui.readID()
                try:
                    self.__ctrl.vaccinate(p)
                except ValueError as ve:
                    print(ve)
                
    @staticmethod
    def readID():
        id=int(input("id:"))
        return id