'''
Created on 6 nov. 2017

@author: Catalin
'''
class NumberController:
    """
    Write specification here
    """
    def __init__(self, repo):
        """
        Write specification here
        """
        self.__repo = repo
        self.__undo = []

    def addNumber(self, number):
        """
        Write specification here
        """
        self.__undo = self.__repo.getAll()[:]
        self.__repo.add(number)

    def remove(self, index):
        """
        Write specification here
        """
        self.__undo = self.__repo.getAll()[:]
        self.__repo.remove(index)

    def removeAll(self, number):
        """
        Write specification here
        """
        self.__undo = self.__repo.getAll()[:]
        while self.__repo.find(number) > -1:
            index = self.__repo.find(number)
            self.__repo.remove(index)

    def getAll(self):
        """
        Write specification here
        """
        return self.__repo.getAll()

    def filterByModulus(self, mod):
        """
        Write specification here
        """
        result = []
        for i in range(0, len(self.__repo)):
            if self.__repo.get(i).modulus() > mod:
                result.append(self.__repo.get(i))
        return result

    def filterByRealPart(self):
        """
        Write specification here
        """
        res = []
        for i in range(0, len(self.__repo)):
            if self.__repo.get(i).getImag() == 0:
                res.append(self.__repo.get(i))
        return res

    def undo(self):
        """
        Write specification here
        """
        if len(self.__undo) == 0:
            raise ControllerException("No undo steps available!")
        
        self.__repo.removeAll()
        for z in self.__undo:
            self.__repo.add(z)
        self.__undo.clear()

class ControllerException(Exception):
    """
    Exception class for controller errors
    """
    def __init__(self, message):
        """
        Constructor for controller exception class
        message - A string representing the exception message
        """
        self.__message = message

    def __str__(self):
        return self.__message