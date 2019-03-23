'''
Created on 1 feb. 2018

@author: Catalin
'''
class resCtrl():
    def __init__(self,resRepo,roomRepo,occRepo):
        self.__resRepo=resRepo
        self.__roomRepo=roomRepo
        self.__occRepo=occRepo
    def addRes(self,r):
        reservations=self.__resRepo.getAll()
        for reservation in reservations:
            if reservation.getRoomNr()==r.getRoomNr():
                raise ValueError("room already occupied!")
        if int(r.getAdate().getMounth())>int(r.getDdate().getMounth()) or (int(r.getAdate().getMounth())==int(r.getDdate().getMounth()) and int(r.getAdate().getDay())>int(r.getDdate().getDay())):
            raise ValueError("invalid dates!")
        self.__resRepo.addRes(r)
    def removeRes(self,idd):
        self.__resRepo.removeRes(idd)
    def addFree(self,r):
        self.__roomRepo.addRoom(r)
    def removeFree(self,nr):
        self.__roomRepo.removeRoom(nr)
    def removeOcc(self,nr):
        self.__occRepo.removeRoom(nr)
    def addOcc(self,r):
        self.__occRepo.addRoom(r)
    def getAllFree(self):
        return self.__roomRepo.getAll()
    def getAllOcc(self):
        return self.__occRepo.getAll()
    def getAllRes(self):
        return self.__resRepo.getAll()