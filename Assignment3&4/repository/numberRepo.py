'''
Created on 6 nov. 2017

@author: Catalin
'''
from domain.complex import Complex

class NumberRepository:

    def __init__(self):
        """
        Constructor for NumberRepository class
        """
        self.__data = []

    def add(self, number):
        """
        Add a number to the repository
        number - Number to be added
        """
        self.__data.append(number)

    def update(self, oldNumber, newNumber):
        """
        Replace the first appearance of oldNumber with newNumber
        oldNumber - The number to be replaced
        newNumber - The updated number
        """
        tmp = []
        for i in range(0, len(self.__data)):
            if self.__data.get(i) != oldNumber:
                tmp.append(self.__data[i])
            else:
                tmp.addNode(newNumber)
        self.__data = tmp

    def find(self, number):
        """
        Return the first index where the given number is found
        number - The number that is searched for
        Returns- The index where the number is first found, -1 otherwise
        """
        for i in range(0, len(self.__data)):
            if self.__data[i] == number:
                return i
        return -1
    
    def __len__(self):
        """
        Overriding the len() built-in function
        """
        return len(self.__data)
    
    def __str__(self):
        """
        String representation of this repository
        """
        s = ""
        for e in self.__data:
            s += str(e) + " "

    def get(self, index):
        """
        Get a number from the repository
        index - Index of the number
        RepositoryException - If an invalid position is given
        """ 
        if index < 0 or index >= len(self.__data):
            raise RepositoryException("Invalid element position")
        return self.__data[index]

    def remove(self, index):
        """
        Remove the entry at the given index from the repository
        index - A natural number between 0 and the repo size
        RepositoryException if the provided index is invalid
        """
        if index < 0 or index >= len(self.__data):
            raise RepositoryException("Invalid element position")
        return self.__data.pop(index)

    def removeAll(self):
        """
        Remove all data from repository 
        """
        self.__data.clear()

    def getAll(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self.__data

class RepositoryException(Exception):
    """
    Exception class for repository errors
    """
    def __init__(self, message):
        """
        Constructor for repository exception class
        message - A string representing the exception message
        """
        self.__message = message

    def __str__(self):
        return self.__message


def testNumberRepository():
    repo = NumberRepository()
    testList = [Complex(1, 2), Complex(0, 1), Complex(2, 3)]
    for i in range(0, len(testList)):
        repo.add(testList[i])
        assert repo.get(i) == testList[i]
    
    for i in range(0, len(testList)):
        assert repo.remove(0) == testList[i]