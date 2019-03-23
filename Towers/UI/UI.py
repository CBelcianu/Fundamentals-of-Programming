'''
Created on 1 feb. 2018

@author: Catalin
'''
from Domain.entities import Reservation,Room,date
from random import randint
class UI():
    def __init__(self,ctrl):
        self.__ctrl=ctrl
    
    @staticmethod
    def printMenu():
        print("\t 1.Create reservation")
        print("\t 2.List all reservations")
        print("\t 3.Delete reservation")
        print("\t 4.Show available rooms")
        
    def main(self):
        keepAlive=True
        while keepAlive:
            UI.printMenu()
            command=input("Enter command").strip()
            if command=='1':
                ok=0
                fn,rt,g,adm,add,ddm,ddd=UI.readRes()
                free=self.__ctrl.getAllFree()
                for room in free:
                    if str(room.getType())==str(rt) and ok==0:
                        resroom=Room(room.getNr(),room.getType())
                        self.__ctrl.removeFree(room.getNr())
                        self.__ctrl.addOcc(resroom)
                        ok=1
                if ok==0:
                    print("no free room of the desired type")
                else:
                    uid=UI.generateUID()
                    try:
                        self.__ctrl.addRes(Reservation(uid,resroom.getNr(),fn,g,date(adm,add),date(ddm,ddd)))
                    except ValueError as ve:
                        print(ve)
            elif command=='2':
                for i in self.__ctrl.getAllRes():
                    print(i)
            elif command=='3':
                idd=UI.readID()
                reservations=self.__ctrl.getAllRes()
                for reservation in reservations:
                    if reservation.getID()==idd:
                        for i in self.__ctrl.getAllOcc():
                            if i.getNr()==reservation.getRoomNr():
                                tip=i.getType()
                        self.__ctrl.removeOcc(reservation.getRoomNr())
                        self.__ctrl.addFree(Room(reservation.getRoomNr(),tip))
                        self.__ctrl.removeRes(idd)
                    else:
                        print("id does not exist")
            elif command=='4':
                for i in self.__ctrl.getAllFree():
                    print(i)
                
    @staticmethod
    def readRes():
        fn=input("family name:")
        rt=input("room type:")
        g=int(input("number of guests:"))
        adm=input("arrival date month (mm):")
        add=input("arrival date month (dd):")
        ddm=input("departure date month (mm):")
        ddd=input("departure date day (dd):")
        return fn,rt,g,adm,add,ddm,ddd
    
    @staticmethod
    def generateUID():
        uid=randint(1000,9999)
        return uid
    
    @staticmethod
    def readID():
        idd=int(input("id (4 digits):"))
        return idd