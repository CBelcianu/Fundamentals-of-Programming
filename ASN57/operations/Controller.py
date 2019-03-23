'''
Created on 11 nov. 2017

@author: Catalin
'''
from operations.UndoController import FunctionCall,Operation,CascadedOperation,UndoController
from domain.entities import Grade
class Controller:
    '''
    implements the program's 'operations'
    Knows only about the repository layer
    '''
    def __init__(self,undoController,repos,repod,repog):
        """
        constructor for StudentController class
        input: repos, repod, repog - repository
        """
        self.__repos=repos
        self.__repod=repod
        self.__repog=repog
        self.__undoController=undoController
    '''
    def undoo(self):
        self.__undoController.undo()
    
    def redoo(self):
        self.__undoController.redo()    
    '''
    def addStudent(self, student, recordForUndo = True):
        if recordForUndo is True:
            undo = FunctionCall(self.removeStudent, student, False)
            redo = FunctionCall(self.addStudent, student, False)
            cascade = CascadedOperation(Operation(undo, redo))
            self.__undoController.recordOperation(cascade)
        self.__repos.add(student)

        
    def removeStudent(self, student, recordForUndo = True):
        '''
        removes a student from the repository and their grades aswell
        input: student - a studentType obj
        '''
        cascade = CascadedOperation()
        #self.__repog.removeGradeStudent(student)
        if recordForUndo is True:
            k=0
            while k<len(self.__repog.getAll()):
                if str(self.__repog.getPos(k).getSID())==str(student.getID()):
                    undo = FunctionCall(self.addGrade, self.__repog.getPos(k),False)
                    redo = FunctionCall(self.removeGrade, self.__repog.getPos(k),False)
                    self.__repog.remove(self.__repog.getPos(k))
                    cascade.add(Operation(undo, redo))
                else:
                    k+=1
            self.__undoController.recordOperation(cascade)
        
        if recordForUndo is True:
            undo = FunctionCall(self.addStudent, student, False)
            redo = FunctionCall(self.removeStudent, student, False)
            cascade.add(Operation(undo, redo))
        self.__repos.remove(student)
    def updateStudent(self, oldStudent, newStudent, recordForUndo = True):
        '''
        updatess a student from the repository
        input: student - a studentType obj
        '''
        if recordForUndo is True:
            undo=FunctionCall(self.updateStudent,newStudent,oldStudent,False)
            redo=FunctionCall(self.updateStudent,oldStudent,newStudent,False)
            cascade = CascadedOperation(Operation(undo, redo))
            self.__undoController.recordOperation(cascade)
        self.__repos.update(oldStudent,newStudent)
    def getAllStudents(self):
        '''
        returns the list of all students
        '''
        return self.__repos.getAll()
    def addDiscipline(self, discipline, recordForUndo = True):
        '''
        adds a discipline to the repository
        input: discipline - a disciplineType obj
        '''
        if recordForUndo is True:
            undo = FunctionCall(self.removeDiscipline, discipline, False)
            redo = FunctionCall(self.addDiscipline, discipline, False)
            cascade = CascadedOperation(Operation(undo, redo))
            self.__undoController.recordOperation(cascade)
        self.__repod.add(discipline)
    def removeDiscipline(self, discipline, recordForUndo = True):
        '''
        removes a discipline from the repository and the grades associated with that discipline
        input: discipline - a disciplineType obj
        '''
        cascade = CascadedOperation()
        #self.__repog.removeGradeDiscipline(discipline)
        if recordForUndo is True:
            k=0
            while k<len(self.__repog.getAll()):
                if str(self.__repog.getPos(k).getSID())==str(discipline.getID()):
                    undo = FunctionCall(self.addGrade, self.__repog.getPos(k),False)
                    redo = FunctionCall(self.removeGrade, self.__repog.getPos(k),False)
                    self.__repog.remove(self.__repog.getPos(k))
                    cascade.add(Operation(undo, redo))
                else:
                    k+=1
            self.__undoController.recordOperation(cascade)
        
        if recordForUndo is True:
            undo = FunctionCall(self.addDiscipline, discipline, False)
            redo = FunctionCall(self.removeStudent, discipline, False)
            cascade.add(Operation(undo, redo))
        self.__repod.remove(discipline)
    def updateDiscipline(self, oldDiscipline,newDiscipline, recordForUndo = True):
        '''
        updates a discipline from the repository
        input: discipline - a disciplineType obj
        '''
        if recordForUndo is True:
            undo=FunctionCall(self.updateDiscipline,newDiscipline,oldDiscipline,False)
            redo=FunctionCall(self.updateDiscipline,oldDiscipline,newDiscipline,False)
            cascade = CascadedOperation(Operation(undo, redo))
            self.__undoController.recordOperation(cascade)
        self.__repod.update(oldDiscipline,newDiscipline)
    def getAllDisciplines(self):
        '''
        returns the list of all disciplines
        '''
        return self.__repod.getAll()
    def addGrade(self, grade, recordForUndo = True):
        '''
        adds a grade to the repository
        input: grade - a gradeType obj
        '''
        ok1=0
        ok2=0
        for i in self.__repos.getAll():
            if i.getID()==grade.getSID():
                ok1=1
        for i in self.__repod.getAll():
            if i.getID()==grade.getDID():
                ok2=1
        if ok1==0 and ok2==0:
            raise ValueError("Student and discipline are inexistent!")
        elif ok1==0:
            raise ValueError("Student does not exist!")
        elif ok2==0:
            raise ValueError("Discipline does not exist!")
        if recordForUndo is True:
            undo = FunctionCall(self.removeGrade, grade, False)
            redo = FunctionCall(self.addGrade, grade, False)
            cascade = CascadedOperation(Operation(undo, redo))
            self.__undoController.recordOperation(cascade)
        self.__repog.add(grade)
    def removeGrade(self, grade, recordForUndo = True):
        self.__repog.remove(grade)
    def getAllGrades(self):
        '''
        returns the list of all existing grades
        '''
        return self.__repog.getAll()
    def findStudentById(self,idd):
        return self.__repos.findById(idd)
    def findDisciplineById(self,idd):
        return self.__repod.findById(idd)
    def findDisciplineByName(self,nem):
        return self.__repod.findByName(nem)
    def findStudentByName(self,nem):
        return self.__repos.findByName(nem)
    def findStudAtDisc(self,discid):
        return self.__repog.studEnrolledDisc(discid)
    def gradeStudDisc(self,studid,discid):
        return self.__repog.gradeStudDisc(studid,discid)
    def failingStud(self,studid):
        return self.__repog.failingStud(studid)
    def gradeStud(self,studid):
        return self.__repog.gradeStud(studid)
    def gradeDisc(self,discid):
        return self.__repog.gradeDisc(discid)