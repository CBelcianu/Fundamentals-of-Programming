'''
Created on 1 feb. 2018

@author: Catalin
'''
'''
Created on 1 feb. 2018

@author: Catalin
'''
class date():
    def __init__(self,d,m):
        self.__d=d
        self.__m=m
    def getDay(self):
        return self.__d
    def getMounth(self):
        return self.__m
    def __str__(self):
        s=''
        s+=self.__m
        s+='.'
        s+=self.__d
        return s

class Room():
    def __init__(self,Nr,Type):
        self.__Nr=Nr
        self.__Type=Type
    def getNr(self):
        return self.__Nr
    def getType(self):
        return self.__Type
    def __str__(self):
        s=''
        s+=str(self.__Nr)
        s+=' '
        s+=str(self.__Type)
        return s
    
class Reservation():
    def __init__(self,ID,roomNr,famName,nrGuests,adate,ddate):
        self.__ID=ID
        self.__roomNr=roomNr
        self.__famName=famName
        self.__nrGuests=nrGuests
        self.__adate=adate
        self.__ddate=ddate
    def getID(self):
        return self.__ID
    def getRoomNr(self):
        return self.__roomNr
    def getFam(self):
        return self.__famName
    def getGuests(self):
        return self.__nrGuests
    def getAdate(self):
        return self.__adate
    def getDdate(self):
        return self.__ddate
    def __str__(self):
        s=''
        s+=str(self.__ID)
        s+=' '
        s+=str(self.__roomNr)
        s+=' '
        s+=str(self.__famName)
        s+=' '
        s+=str(self.__nrGuests)
        s+=' '
        s+=str(self.__adate)
        s+=' '
        s+=str(self.__ddate)
        return s