'''
Created on 12 dec. 2017

@author: Catalin
'''
from repository.entitiesRepository import studentRepository,gradeRepository,disciplineRepository
from domain.entities import Student,Discipline,Grade
import pickle
class StudentCSVFileRepository(studentRepository):
    def __init__(self, fileName="students.txt"):
        studentRepository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
    
    def add(self, student):
        studentRepository.add(self, student)
        self.__storeToFile()
    
    def remove(self, student):
        studentRepository.remove(self, student)
        self.__storeToFile()        
    
    def update(self,oldStudent, newStudent):
        studentRepository.update(self,oldStudent, newStudent)
        self.__storeToFile()
    
    def __loadFromFile(self):
        f = open(self.__fName, "r")
        line = f.readline().strip()
        while line != "":
            attrs = line.split(",")
            student = Student(int(attrs[0]), attrs[1])
            studentRepository.add(self, student)
            line = f.readline().strip()
        f.close()
        
    def __storeToFile(self):
        f = open(self.__fName, "w")
        students = studentRepository.getAll(self)
        for student in students:
            strf = str(student.getID()) + "," + student.getName() + "\n"
            f.write(strf)
        f.close()

class DisciplineCVSFileRepository(disciplineRepository):
    def __init__(self, fileName="disciplines.txt"):
        disciplineRepository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
    
    def add(self, discipline):
        disciplineRepository.add(self, discipline)
        self.__storeToFile()
    
    def remove(self, discipline):
        disciplineRepository.remove(self, discipline)
        self.__storeToFile()        
    
    def update(self,oldDiscipline, newDiscipline):
        disciplineRepository.update(self,oldDiscipline, newDiscipline)
        self.__storeToFile()
    
    def __loadFromFile(self):
        f = open(self.__fName, "r")
        line = f.readline().strip()
        while line != "":
            attrs = line.split(",")
            discipline = Discipline(int(attrs[0]), attrs[1])
            disciplineRepository.add(self, discipline)
            line = f.readline().strip()
        f.close()
        
    def __storeToFile(self):
        f = open(self.__fName, "w")
        disciplines = disciplineRepository.getAll(self)
        for discipline in disciplines:
            strf = str(discipline.getID()) + "," + discipline.getName() + "\n"
            f.write(strf)
        f.close()
        
class GradeCVSFileRepository(gradeRepository):
    def __init__(self, fileName="grades.txt"):
        gradeRepository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
    
    def add(self, grade):
        gradeRepository.add(self, grade)
        self.__storeToFile()
    
    def remove(self, grade):
        gradeRepository.remove(self, grade)
        self.__storeToFile()        
    
    def __loadFromFile(self):
        f = open(self.__fName, "r")
        line = f.readline().strip()
        while line != "":
            attrs = line.split(",")
            grade = Grade(int(attrs[0]), int(attrs[1]), int(attrs[2]))
            gradeRepository.add(self, grade)
            line = f.readline().strip()
        f.close()
        
    def __storeToFile(self):
        f = open(self.__fName, "w")
        grades = gradeRepository.getAll(self)
        for grade in grades:
            strf = str(grade.getDID()) + "," + str(grade.getSID()) +","+ str(grade.getValue()) + "\n"
            f.write(strf)
        f.close()
class StudentPickleFileRepository(studentRepository):
    def __init__(self, fileName="stud.pickle"):
        studentRepository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
    
    def add(self, student):
        studentRepository.add(self, student)
        self.__storeToFile()
     
    def remove(self, student):
        studentRepository.remove(self, student)
        self.__storeToFile()        
 
    def update(self, oldStudent,newStudent):
        studentRepository.update(self, oldStudent,newStudent)
        self.__storeToFile()

    def __loadFromFile(self):
        with open(self.__fName, "rb") as f:
            try:
                studentRepository.overwrite(self, pickle.load(f))
            except EOFError:
                self._data = []
            except Exception as e:
                raise e
            finally:
                f.close()

    def __storeToFile(self):
        with open(self.__fName, "wb") as f:
            pickle.dump(studentRepository.getAll(self),f)
            f.close()
class DisciplinePickleFileRepository(disciplineRepository):
    def __init__(self, fileName="disc.pickle"):
        disciplineRepository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
    
    def add(self, discipline):
        disciplineRepository.add(self, discipline)
        self.__storeToFile()
     
    def remove(self, discipline):
        disciplineRepository.remove(self, discipline)
        self.__storeToFile()        
 
    def update(self, oldDiscipline,newDiscipline):
        disciplineRepository.update(self, oldDiscipline,newDiscipline)
        self.__storeToFile()

    def __loadFromFile(self):
        with open(self.__fName, "rb") as f:
            try:
                disciplineRepository.overwrite(self, pickle.load(f))
            except EOFError:
                self._data = []
            except Exception as e:
                raise e
            finally:
                f.close()

    def __storeToFile(self):
        with open(self.__fName, "wb") as f:
            pickle.dump(disciplineRepository.getAll(self), f)
            f.close()
class GradePickleFileRepository(gradeRepository):
    def __init__(self, fileName="grd.pickle"):
        gradeRepository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
    
    def add(self, grade):
        gradeRepository.add(self, grade)
        self.__storeToFile()
     
    def remove(self, grade):
        gradeRepository.remove(self, grade)
        self.__storeToFile()

    def __loadFromFile(self):
        with open(self.__fName, "rb") as f:
            try:
                gradeRepository.overwrite(self, pickle.load(f))
            except EOFError:
                self._data = []
            except Exception as e:
                raise e
            finally:
                f.close()

    def __storeToFile(self):
        with open(self.__fName, "wb") as f:
            pickle.dump(gradeRepository.getAll(self), f)
            f.close()