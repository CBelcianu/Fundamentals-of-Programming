'''
Created on 13 dec. 2017

@author: Catalin
'''
from domain.entities import Student, Discipline, Grade
class myDataStructure():
    def __init__(self):
        self.__data=[]
        self.__index=0
    def __iter__(self):
        return self
    def __next__(self):
        try:
            itm=self.__data[self.__index]
        except IndexError:
            raise StopIteration
        self.__index+=1   
        return itm
    def __len__(self):
        return len(self.__data)
    def __getitem__(self,index):
        return self.__data[index]
    def __setitem__(self,index,value):
        self.__data[index]=value
    def append(self,x):
        self.__data.append(x)
    def pop(self,index):
        return self.__data.pop(index)
    def sorted(self,key=lambda x:x,cmp=lambda x,y:x<y):
        index = 0
        while index < len(self.__data):
            if index == 0:
                index = index + 1
            if cmp(key(self.__data[index]),key(self.__data[index - 1])):
                index = index + 1
            else:
                self.__data[index], self.__data[index-1] = self.__data[index-1], self.__data[index]
                index = index - 1
        return self.__data
'''         
x=myDataStructure()
x.append(Grade(7,7,9))
x.append(Grade(2,5,2))
x.append(Grade(5,6,4))
x.append(Grade(9,2,10))
x.append(Grade(1,3,8))
x.append(Grade(3,4,1))
x.sorted(lambda x:x, lambda x,y:x.getSID()<y.getSID())
for i in x:
    print(i)

'''
x=myDataStructure()
x.append(Student(7,"Andrei"))
x.append(Student(2,"Vlad"))
x.append(Student(5,"Bogdan"))
x.append(Student(9,"Razvan"))
x.append(Student(1,"Ion"))
x.append(Student(3,"Zack"))
x.sorted()
for i in x:
    print(i)
