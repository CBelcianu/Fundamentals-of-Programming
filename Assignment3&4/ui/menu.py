'''
Created on 6 nov. 2017

@author: Catalin
'''
from domain.complex import Complex

class UI:
    def __init__(self, controller):
        self._controller = controller

    @staticmethod
    def printMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1 - Add number\n'
        string += '\t 2 - Remove number at position\n'
        string += '\t 3 - Remove all number appearances\n'
        string += '\t 4 - Display numbers\n'
        string += '\t 5 - Display numbers with modulus>value\n'
        string += '\t 6 - Display real numbers\n'
        string += '\t 8 - Undo\n'
        string += '\t 0 - Exit\n'
        print(string)

    def mainMenu(self):
        keepAlive = True
        while keepAlive:
            try:
                UI.printMenu()
                command = input("Enter command: ").strip()
                if command == '0':
                    print("exit...")
                    keepAlive = False
                elif command == '1':
                    z = UI.readComplexNumber()
                    self._controller.addNumber(z)
                elif command == '2':
                    p = self.readPositiveInteger("Please give position:")
                    try:
                        self._controller.remove(p)
                    except Exception as ve:
                        print(ve)
                elif command == '3':
                    z = self.readComplexNumber()
                    self._controller.removeAll(z)
                elif command == '4':
                    for n in self._controller.getAll():
                        print(str(n))
                elif command == '5':
                    v = self.readPositiveInteger("Please give modulus:")
                    UI.printList(self._controller.filterByModulus(v))
                elif command == '6':
                    UI.printList(self._controller.filterByRealPart())
                elif command == '8':
                    self._controller.undo()
                else:
                    print("Invalid commnad!")
            except Exception as exc:
                print("Error encountered - "+str(exc))

    @staticmethod
    def printList(l):
        print("List is:")
        for z in l:
            print(str(z))

    @staticmethod
    def readPositiveInteger(msg):
        """
        Reads a positive integer
        Input: -
        Output: A positive integer
        """
        result = None
        while result == None:
            try:
                result = int(input(msg))
                if result < 0:
                    raise ValueError
            except ValueError:
                print("Please input a positive integer!")
        return result

    @staticmethod
    def readComplexNumber():
        """
        Reads a complex number
        Input:  -
        Output: The complex number
        Exceptions: -
        """
        while True:
            try:
                r = int(input("Real part="))
                i = int(input("Imag part="))
                return Complex(r, i)
            except ValueError:
                print("Real/Imag parts must be numbers!")
        return []