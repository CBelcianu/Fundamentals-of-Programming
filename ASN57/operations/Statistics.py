'''
Created on 16 dec. 2017

@author: Catalin
'''
from operator import itemgetter

class Statistics:
    def __init__(self,controller):
        self._controller=controller
    def AllStudentsEnrolledAtDiscipline(self):
        sl=[]
        print("enter the discipline id")
        d=Statistics.readID()
        print("\t1.list students sorted alphabetically")
        print("\t2.list students sorted descending by the average grade")
        cmd=input("select the list method:").strip()
        if cmd=='1':
            sl1=[]
            sl=self._controller.findStudAtDisc(d)
            for i in sl:
                s=self._controller.findStudentById(i)
                sl1.append([i,s.getName()])
            sl1=sorted(sl1,key=itemgetter(1))
            if not sl1:
                print("there is no students enrolled at this discipline")
            else:
                for i in sl1:
                    print("ID:",i[0],"Name:",i[1])
        elif cmd=='2':
            sl1=[]
            sl=self._controller.findStudAtDisc(d)
            for i in sl:
                s=self._controller.findStudentById(i)
                g=self._controller.gradeStudDisc(i,d)
                sl1.append([i,s.getName(),g])
            sl1=reversed(sorted(sl1,key=itemgetter(2)))
            for i in sl1:
                print("ID:",i[0],"Name:",i[1],"Average grade:",i[2])
    def FailingStuds(self):
        msj=''
        for s in self._controller.getAllStudents():
            gl=self._controller.failingStud(s.getID())
            if len(gl)>0:
                if len(gl)==1:
                    print("student with id:",s.getID(),"and name:",s.getName(),"is failing at",self._controller.findDisciplineById(gl[0][0]).getName(),"with average grade",gl[0][1])
                else:
                    k=0
                    tmp=[]
                    while k<len(gl):
                        if k!=0:
                            msj+=", "
                        tmp.append(self._controller.findDisciplineById(gl[k][0]).getName())
                        tmp.append(gl[k][1])
                        k=k+1
                        msj+=str(tmp[-2])+" with average grade "+str(tmp[-1])
                    print("student with id:",s.getID(),"and name:",s.getName(),"is failing at",msj)
    def BestSchoolSitutaion(self):
        sl=[]
        for s in self._controller.getAllStudents():
            if self._controller.gradeStud(s.getID()) > 0:
                sl.append([s.getID(),s.getName(),self._controller.gradeStud(s.getID())])
        sl=reversed(sorted(sl,key=itemgetter(2)))
        for i in sl:
            print("ID:",i[0],"Name:",i[1],"Aggregated average grade:",i[2])  
    def ActDisc(self):
        for d in self._controller.getAllDisciplines():
            g=self._controller.gradeDisc(d.getID())
            if g>0:
                print("ID:",d.getID(),"Name:",d.getName(),"Average of all grades received by all students:",g)
    @staticmethod
    def readID():
        '''
        reads an id
        '''
        uid=int(input("id:"))
        return uid
        