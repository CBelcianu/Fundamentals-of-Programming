'''
Created on 11 nov. 2017

@author: Catalin
'''
class Student():
    '''
    s=[stundentID,studentNAME]
    '''
    def __init__(self,ID,name):
        """
        constructor for Student class
        cnput: ID,name - ID of the student and his name respectively
        """
        self._ID=ID
        self._name=name
    def __str__(self):
        r=''
        r+=str(self._ID)
        r+=' '
        r+=str(self._name)
        return r
    def __lt__(self,other):
        if isinstance(other,self.__class__):
            return self._ID<other._ID
        else:
            return False
    def getID(self):
        return int(self._ID)
    def getName(self):
        return self._name

class Discipline():
    '''
    d=[disciplineID,disciplineNAME]
    '''
    def __init__(self,ID,name):
        """
        constructor for Discipline class
        cnput: ID,name - ID of the discipline and its name respectively
        """
        self._ID=ID
        self._name=name
    def __str__(self):
        r=''
        r+=str(self._ID)
        r+=' '
        r+=str(self._name)
        return r
    def __lt__(self,other):
        if isinstance(other,self.__class__):
            return self._ID<other._ID
        else:
            return False
    def getID(self):
        return int(self._ID)
    def getName(self):
        return self._name

class Grade():
    '''
    g=[disciplineID,stundentID,value]
    '''
    def __init__(self,dID,sID,value):
        """
        constructor for Grade class
        cnput: dID,sID,value - ID of the discipline, ID of the student and the value of the grade
        """
        self._sID=sID
        self._dID=dID
        self._value=value
    def __str__(self):
        r=''
        r+=str(self._dID)
        r+=' '
        r+=str(self._sID)
        r+=' '
        r+=str(self._value)
        return r
    def __lt__(self,other):
        if isinstance(other,self.__class__):
            return self._value<other._value
        else:
            return False
    def getSID(self):
        return int(self._sID)
    def getDID(self):
        return int(self._dID)
    def getValue(self):
        return int(self._value)