'''
Created on 19 dec. 2017

@author: Catalin
'''
class route:
    def __init__(self,ID,Dist):
        self.__ID=ID
        self.__Dist=Dist
    def getID(self):
        return self.__ID
    def getDist(self):
        return self.__Dist
    def __str__(self):
        s=''
        s+=str(self.__ID)
        s+=' '
        s+=str(self.__Dist)
        return s
    
class bus:
    def __init__(self,bID,rID,model,times):
        self.__bID=bID
        self.__rID=rID
        self.__model=model
        self.__times=times
    def getBID(self):
        return self.__bID
    def getRID(self):
        return self.__rID
    def getModel(self):
        return self.__model
    def getTimes(self):
        return self.__times
    def __str__(self):
        s=''
        s+=str(self.__bID)
        s+=' '
        s+=str(self.__rID)
        s+=' '
        s+=str(self.__model)
        s+=' '
        s+=str(self.__times)
        return s