'''
Created on 4 dec. 2017

@author: Catalin
'''
class UndoController:

    def __init__(self):
        self._history = []
        self._index = -1
        self._recorded = True

    def recordOperation(self, cascadedOp):
        '''
        Record the operation for undo/redo
        '''
        self._history.append(cascadedOp)
        self._index += 1

    def undo(self):
        '''
        Undo the last operation
        '''
        if self._index >= 0:
            self._history[self._index].undo()
            self._index -= 1

    def redo(self):
        '''
        Redo the last operation
        Return True if successful, False otherwise
        '''
        if self._index < len(self._history) - 1:
            self._history[self._index+1].redo()
            self._index += 1
            return True
        return False

class FunctionCall:
    def __init__(self, functionRef, *parameters):
        self._functionRef = functionRef
        self._parameters = parameters

    def call(self):
        self._functionRef(*self._parameters)

class Operation:
    def __init__(self, functionUndo, functionDo):
        self._functionUndo = functionUndo
        self._functionDo = functionDo

    def undo(self):
        self._functionUndo.call()

    def redo(self):
        self._functionDo.call()

class CascadedOperation:
    def __init__(self, op=None):
        self._operations = []

        if op != None:
            self.add(op)

    def add(self, op):
        self._operations.append(op)

    def undo(self):
        for i in range(len(self._operations) - 1, -1, -1):
            self._operations[i].undo()

    def redo(self):
        for i in range(len(self._operations) - 1, -1, -1):
            self._operations[i].redo()