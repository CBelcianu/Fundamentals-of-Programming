'''
Created on 11 nov. 2017

@author: Catalin
'''
from repository.entitiesRepository import studentRepository, disciplineRepository, gradeRepository
from operations.Controller import Controller
from ui.menu import UI
from domain.entities import Student,Discipline,Grade
from operations.UndoController import UndoController
from repository.fileRepository import StudentCSVFileRepository, DisciplineCVSFileRepository, GradeCVSFileRepository, StudentPickleFileRepository, DisciplinePickleFileRepository, GradePickleFileRepository
print("\t 1.run the program in memory")
print("\t 2.run the program using text files")
print("\t 3.run the program using pickle files")
command = input(">>").strip()
if command=='2':
    repos = StudentCSVFileRepository()
    repod = DisciplineCVSFileRepository()
    repog = GradeCVSFileRepository()
    undoCtrl = UndoController()
elif command=='3':
    repos = StudentPickleFileRepository("stud.pickle")
    repod = DisciplinePickleFileRepository("disc.pickle")
    repog = GradePickleFileRepository("grd.pickle")
    undoCtrl = UndoController()
elif command=='1':
    repos = studentRepository()
    repod = disciplineRepository()
    repog = gradeRepository()
    undoCtrl = UndoController()
    #initialize repository
    repos.add(Student(1, "Vasile"))
    repos.add(Student(2, "Razvan"))
    repos.add(Student(3, "Victor"))
    repos.add(Student(4, "Ion"))
    repos.add(Student(5, "George"))
    repos.add(Student(6, "Andrei"))
    repos.add(Student(7, "Alex"))
    repos.add(Student(8, "Vlad Andrei"))
    repos.add(Student(9, "Adrian"))
    repos.add(Student(10, "Razvan"))
    repos.add(Student(11, "Razvan Andrei"))
    repod.add(Discipline(1, "Fizica"))
    repod.add(Discipline(2, "Matematica"))
    repod.add(Discipline(3, "Romana"))
    repod.add(Discipline(4, "Informatica"))
    repod.add(Discipline(5, "Chimie"))
    repod.add(Discipline(6, "Engleza"))
    repod.add(Discipline(7, "Franceza"))
    repod.add(Discipline(8, "Matematica aplicata"))
    repog.add(Grade(2,2,9))
    repog.add(Grade(2,2,8))
    repog.add(Grade(1,2,9))
    repog.add(Grade(1,1,10))
    repog.add(Grade(3,4,9))
    repog.add(Grade(4,4,10))
    repog.add(Grade(3,4,3))
    repog.add(Grade(4,4,2))
    repog.add(Grade(3,4,2))
    repog.add(Grade(4,4,3))
    repog.add(Grade(1,1,2))
    repog.add(Grade(1,1,2))
    repog.add(Grade(1,1,3))
    repog.add(Grade(2,1,2))
    repog.add(Grade(2,1,2))
    repog.add(Grade(2,1,3))
    
#initialize controller
controller = Controller(undoCtrl,repos,repod,repog)
#initialize user interface
ui = UI(controller,undoCtrl)
#start
ui.mainMenu()