'''
Created on 11 nov. 2017

@author: Catalin
'''
from domain.entities import Student, Discipline, Grade
from operator import itemgetter
from operations.UndoController import UndoController
from operations.Statistics import Statistics
class UI:
    def __init__(self, controller,UndoController):
        self._controller = controller
        self._undoController = UndoController
    @staticmethod
    def printMenu():
        '''
        prints the menu
        '''
        string = '\nAvailable commands:\n'
        string += '\t 1 - Add Student\n'
        string += '\t 2 - List Students\n'
        string += '\t 3 - Remove Student\n'
        string += '\t 4 - Update Student\n'
        string += '\t 5 - Add Discipline\n'
        string += '\t 6 - List Discipline\n'
        string += '\t 7 - Remove Discipline\n'
        string += '\t 8 - Update Discipline\n'
        string += '\t 9 - Add a grade\n'
        string += '\t 10 - Show the grades of a certain student\n'
        string += '\t 11 - Show the all the grades at a certain discipline\n'
        string += '\t 12 - Search for students/disciplines\n'
        string += '\t 13 - List all students enrolled at a certain discipline\n'
        string += '\t 14 - List students failing at one or more disciplines\n'
        string += '\t 15 - List the students with the best school situation\n'
        string += '\t 16 - List all disciplines at which there is at least one grade\n'
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
                    s = UI.readStudent()
                    self._controller.addStudent(s)
                elif command == '2':
                    for n in self._controller.getAllStudents():
                        print("ID: "+str(n.getID())+" Name: "+n.getName())
                elif command == '3':
                    i=UI.readID()
                    #s = UI.readStudent()
                    s=self._controller.findStudentById(i)
                    self._controller.removeStudent(s)
                elif command == '4':
                    print("enter the old Student")
                    os=UI.readStudent()
                    print("enter the new Student")
                    ns=UI.readStudent()
                    if(os._ID!=ns._ID):
                        print("Error encountered - the id should be the same!")
                    else:
                        self._controller.updateStudent(os,ns)
                elif command == '5':
                    d = UI.readDiscipline()
                    self._controller.addDiscipline(d)
                elif command == '6':
                    for n in self._controller.getAllDisciplines():
                        print("ID: "+str(n.getID())+" Name: "+n.getName())
                elif command == '7':
                    i=UI.readID()
                    #d=UI.readDiscipline()
                    d=self._controller.findDisciplineById(i)
                    self._controller.removeDiscipline(d)
                elif command == '8':
                    print("enter the old discipline")
                    od=UI.readDiscipline()
                    print("enter the new discipline")
                    nd=UI.readDiscipline()
                    if(od._ID!=nd._ID):
                        print("Error encountered - the id should be the same!")
                    else:
                        self._controller.updateDiscipline(od,nd)
                elif command == '9':
                    g=UI.readGrade()
                    self._controller.addGrade(g)
                elif command == '10':
                    k=0
                    s=UI.readID()
                    for n in self._controller.getAllGrades():
                        if n.getSID()==s:
                            n=str(n)
                            n=n.split()
                            for d in self._controller.getAllDisciplines():
                                if str(d.getID())==str(n[0]):
                                    print(n[2],"at",d.getName())
                                    k=1
                    if k==0:
                        print("the student has no grades!")
                elif command == '11':
                    k=0
                    d=UI.readID()
                    for n in self._controller.getAllGrades():
                        if n.getDID()==d:
                            n=str(n)
                            n=n.split()
                            for x in self._controller.getAllStudents():
                                if str(x.getID())==str(n[1]):
                                    print(n[2],x.getName())
                            k=1
                    if k==0:
                        print("there is no grade at this discipline!")
                elif command == '12':
                    print("\t 1.search for students and disciplines by ID \t 2.search for students by name \t 3.search for disciplines by title")
                    cmd=input("select the search method:").strip()
                    if cmd=='1':
                        uid=UI.readID()
                        print(self._controller.findStudentById(uid).getName())
                        print(self._controller.findDisciplineById(uid).getName())
                    elif cmd=='2':
                        try:
                            nem=UI.readName()
                            sl=self._controller.findStudentByName(nem)
                            for i in sl:
                                print("ID: "+str(i.getID())+" Name: "+i.getName())
                        except ValueError as ve:
                            print(ve)
                    elif cmd=='3':
                        try:
                            nem=UI.readName()
                            dl=self._controller.findDisciplineByName(nem)
                            for i in dl:
                                print("ID: "+str(i.getID())+" Name: "+i.getName())
                        except ValueError as ve:
                            print(ve)
                elif command=='13':
                    st=Statistics(self._controller)
                    st.AllStudentsEnrolledAtDiscipline()   
                elif command=='14':
                    st=Statistics(self._controller)
                    st.FailingStuds()
                elif command=='15':
                    st=Statistics(self._controller)
                    st.BestSchoolSitutaion()
                elif command=='16':
                    st=Statistics(self._controller)
                    st.ActDisc()
                elif command=='17':
                    self._undoController.undo()
                elif command=='18':
                    self._undoController.redo()
                elif command=='19':
                    self._controller.removeGrade(Grade(1,1,1),False)
                else:
                    print("INVALID COMMAND!")   
            except Exception as exc:
                print("Error encountered - "+str(exc)) 
    @staticmethod
    def readID():
        '''
        reads an id
        '''
        uid=int(input("id:"))
        return uid
                      
    @staticmethod
    def readStudent():
        '''
        reads a studentType object from the keyboard
        '''
        uid=int(input("student id:"))
        name=input("student name: ")
        return Student(uid,name)
    @staticmethod
    def readDiscipline():
        '''
        reads a disciplineType object from the keyboard
        '''
        uid=int(input("discipline id: "))
        name=input("discipline name: ")
        return Discipline(uid,name)
    @staticmethod
    def readGrade():
        '''
        reads o gradeType object from the keyboard
        '''
        print("student:")
        s=UI.readID()
        print("discipline:")
        d=UI.readID()
        grade=int(input("grade: "))
        return Grade(d,s,grade)
    @staticmethod
    def readName():
        '''
        reads a name from the KeyboardInterrup
        '''
        name=input("name:")
        n1=name.split()
        if len(n1)>1:
            raise ValueError("You cand only read one name/title (without blanks)!")
        else:
            return name