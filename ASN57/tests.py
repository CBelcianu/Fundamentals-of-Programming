'''
Created on 22 nov. 2017

@author: Catalin
'''
import unittest
from repository.entitiesRepository import studentRepository, disciplineRepository, gradeRepository
from domain.entities import Discipline, Grade, Student

class Test(unittest.TestCase):
    def testStundet(self):
        repos=studentRepository()
        repos.add(Student(1,"Vasile"))
        self.assertEqual( str(repos.getPos(0)),str(Student(1,"Vasile")) )
        repos.add(Student(2,"Ion"))
        self.assertEqual( str(repos.getPos(1)),str(Student(2,"Ion")) )
        repos.remove(Student(2,"Ion"))
        self.assertEqual( str(repos.getPos(0)),str(Student(1,"Vasile")) )
        repos.update(Student(1,"Vasile"), Student(1,"Ion"))
        self.assertEqual( str(repos.getPos(0)),str(Student(1,"Ion")) )
    def testDiscipline(self):
        repod=disciplineRepository()
        repod.add(Discipline(1,"Info"))
        self.assertEqual( str(repod.getPos(0)),str(Discipline(1,"Info")) )
        repod.add(Discipline(2,"Mate"))
        self.assertEqual( str(repod.getPos(1)),str(Discipline(2,"Mate")) )
        repod.remove(Discipline(2,"Mate"))
        self.assertEqual( str(repod.getPos(0)),str(Discipline(1,"Info")) )
        repod.update(Discipline(1,"Info"), Discipline(1,"FP"))
        self.assertEqual( str(repod.getPos(0)),str(Discipline(1,"FP")) )
    def testGrade(self):
        repog=gradeRepository()
        repog.add(Grade(1,1,9))
        self.assertEqual( str(repog.getPos(0)),str(Grade(1,1,9)) )
        repog.add(Grade(1,1,8))
        self.assertEqual( str(repog.getPos(1)),str(Grade(1,1,8)) )
        repog.add(Grade(2,2,9))
        self.assertEqual( str(repog.getPos(2)),str(Grade(2,2,9)) )
        repog.removeGradeStudent(Student(2,"Razvan"))
        self.assertEqual( str(repog.getPos(1)),str(Grade(1,1,8)) )
        repog.add(Grade(2,2,9))
        self.assertEqual( str(repog.getPos(2)),str(Grade(2,2,9)) )
        repog.removeGradeDiscipline(Discipline(1,"Fizica"))
        self.assertEqual( str(repog.getPos(0)),str(Grade(2,2,9)) )
        
        

        