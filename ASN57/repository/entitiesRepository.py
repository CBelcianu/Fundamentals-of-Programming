'''
Created on 11 nov. 2017

@author: Catalin
'''
from domain.entities import Student,Discipline,Grade
from myDataSturucture import myDataStructure
class studentRepository():
    '''
    implements the program's "repository" for "Student" obj
    Knows only about the domain layer
    '''
    def __init__(self):
        '''
        constructor for Controller class
        input: __data - list
        '''
        self.__data=myDataStructure()
    def overwrite(self,lista):
        self.__data=lista
    def add(self, student):
        '''
        adds a student to the repository
        input: student
        '''
        for n in student.getName():
            if n.isdigit()==True:
                raise ValueError("invalid name")
        for i in range(0, len(self.__data)):
            if str(self.__data[i].getID())==str(student.getID()):
                raise ValueError("id already exists")
        self.__data.append(student)
    def update(self, oldStudent, newStudent):
        '''
        updates a student from the repository
        input: oldStudent, newStudent
        '''
        for i in range(0, len(self.__data)):
            if str(self.__data[i]) == str(oldStudent):
                self.__data[i] = newStudent
    def remove(self, student):
        '''
        removes a student from the repository
        input: student
        '''
        i=0
        while student.getID()!=self.__data[i].getID():
            i+=1
        return self.__data.pop(i)
    def getAll(self):
        '''
        returns all the students from the repository
        '''
        return self.__data[0:len(self.__data)]
    def __len__(self):
        return len(self.__data)
    def __str__(self):
        s = ""
        for e in self.__data[0:len(self.__data)]:
            s += str(e) + " "
        return s
    def findById(self,idd):
        for i in self.__data[0:len(self.__data)]:
            if i.getID()==idd:
                return i
    def getPos(self,i):
        '''
        returns the student at position i from the repository
        input: i
        '''
        if i < 0 or i >= len(self.__data):
            raise ValueError("Invalid element position")
        return self.__data[i]
    def findByName(self,nem):
        sl=[]
        for s in self.__data[0:len(self.__data)]:
            s1=s.getName().split()
            for s2 in s1:
                if nem.lower() in s2.lower():
                    sl.append(s)
                    break
        return sl

class disciplineRepository():
    '''
    implements the program's "repository" for "Discipline" obj
    Knows only about the domain layer
    '''
    def __init__(self):
        '''
        constructor for Controller class
        input: __data - list
        '''
        self.__data=myDataStructure()
    def overwrite(self,lista):
        self.__data=lista
    def add(self, discipline):
        '''
        adds a discipline to the repository
        input: discipline
        '''
        for i in range(0,len(self.__data)):
            if int(self.__data[i].getID()==int(discipline.getID())):
                raise ValueError("id already exists")
        self.__data.append(discipline) 
    def update(self, oldDiscipline, newDiscipline):
        '''
        updates a discipline from the repository
        input: oldDiscipline, newDiscipline
        '''
        for i in range(0,len(self.__data)):
            if str(self.__data[i])==str(oldDiscipline):
                self.__data[i]=newDiscipline
    def remove(self,discipline):
        '''
        removes a discipline from the repository
        input: discipline
        '''
        i=0
        while discipline.getID()!=self.__data[i].getID():
            i+=1
        return self.__data.pop(i)
    def getAll(self):
        '''
        returns all the disciplines from the repository
        '''
        return self.__data[0:len(self.__data)]
    def __len__(self):
        return len(self.__data)
    def __str__(self):
        s = ""
        for e in self.__data[0:len(self.__data)]:
            s += str(e) + " "
        return s
    def getPos(self,i):
        '''
        returns the discipline at position i in the repository
        input: i
        '''
        if i < 0 or i >= len(self.__data):
            raise ValueError("Invalid element position")
        return self.__data[i]
    def findById(self,idd):
        for i in self.__data[0:len(self.__data)]:
            if i.getID()==idd:
                return i
    def findByName(self,nem):
        dl=[]
        for d in self.__data[0:len(self.__data)]:
            d1=d.getName().split()
            for d2 in d1:
                if nem.lower() in d2.lower():
                    dl.append(d)
                    break
        return dl
    
class gradeRepository():
    '''
    implements the program's "repository" for "Grade" obj
    Knows only about the domain layer
    '''
    def __init__(self):
        '''
        constructor for Controller class
        input: __data - list
        '''
        self.__data=myDataStructure()
    def overwrite(self,lista):
        self.__data=lista
    def add(self, grade):
        '''
        adds a grade to the repository
        input: grade
        '''
        if int(grade._value)>10 or int(grade._value)<0:
            raise ValueError("invalid grade!")
        self.__data.append(grade)
    def remove(self, grade):
        n=0
        while n<len(self.__data):
            if str(self.__data[n])==str(grade):
                self.__data.pop(n)
                break
            n+=1
    def getAll(self):
        '''
        returns all the grades from the repository
        '''
        return self.__data[0:len(self.__data)]
    """
    def removeGradeStudent(self, student):
        n=0
        while n<len(self.__data):
            if str(self.__data[n].getSID())==str(student.getID()):
                self.__data.pop(int(n))
                n-=1
            n+=1
    def removeGradeDiscipline(self, discipline):
        n=0
        while n<len(self.__data):
            if str(self.__data[n].getDID())==str(discipline.getID()):
                self.__data.pop(int(n))
                n-=1
            n+=1
    """
    def getPos(self,i):
        '''
        returns the grade at position i in the repository
        input: i
        '''
        if i < 0 or i >= len(self.__data):
            raise ValueError("Invalid element position")
        return self.__data[i]
    def studEnrolledDisc(self,discid):
        sl=[]
        for g in self.__data[0:len(self.__data)]:
            if g.getDID()==discid:
                if g.getSID() in sl:
                    pass
                else:
                    sl.append(g.getSID())
        return sl
    def gradeStudDisc(self,studid,discid):
        s=0
        k=0
        for g in self.__data[0:len(self.__data)]:
            if g.getSID()==studid and g.getDID()==discid:
                s=s+g.getValue()
                k=k+1
        if k!=0:
            return float(s/k)
        else:
            return 0
    def failingStud(self,studid):
        gl=[]
        dl=[]
        for g in self.__data[0:len(self.__data)]:
            if g.getDID() in dl:
                pass
            else:
                dl.append(g.getDID())
        for d in dl:
            s=0
            k=0
            for g in self.__data[0:len(self.__data)]:
                if g.getSID()==studid and g.getDID()==d:
                    s=s+g.getValue()
                    k=k+1
            if k!=0:        
                if s/k<5:
                    gl.append([d,float(s/k)])
        return gl
    def gradeStud(self,studid):
        s=0
        k=0
        for g in self.__data[0:len(self.__data)]:
            if g.getSID()==studid:
                s=s+g.getValue()
                k=k+1
        if k!=0:
            return float(s/k)
        else:
            return 0
    def gradeDisc(self,discid):
        s=0
        k=0
        for g in self.__data[0:len(self.__data)]:
            if g.getDID()==discid:
                s=s+g.getValue()
                k=k+1
        if k!=0:
            return float(s/k)
        else:
            return 0
    