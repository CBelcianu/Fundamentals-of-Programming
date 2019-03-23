'''
Created on 28 dec. 2017

@author: Catalin
'''
from random import randint
class square:
    '''
    represents a square of the table
    '''
    def __init__(self,x,y):
        '''
        input:x,y-coordinates
        '''
        self.__x=x
        self.__y=y
    def getX(self):
        '''
        returns the x coord
        '''
        return self.__x
    def getY(self):
        '''
        returns the y coord
        '''
        return self.__y
    
class board():
    def __init__(self,c,r):
        '''
        constructor for board class
        input: c-no. of columns and r-no. of rows
        '''
        l1=[]
        l2=[]
        for i in range(0,r):
            for i in range(0,c):
                l1.append('0')
            l2.append(l1)
            l1=[]
        self.__data=l2
        self.__col=c
        self.__row=r
    def getData(self):
        '''
        returns the list of the values of squares
        '''
        return self.__data
    def getC(self):
        '''
        returns the number of columns of the board
        '''
        return self.__col
    def getR(self):
        '''
        returns the nuber of rows of the board
        '''
        return self.__row
    def __str__(self):
        str1='\n'
        str1+='  '
        for  i in range(0,self.__col):
            str1+=str(i+1)+' '
        str1+='\n'
        r=0
        l=0
        for i in self.__data:
            str1+=str(r+1)+' '
            r+=1
            l=0
            for j in i:
                l+=1
                if j=='0':
                    str1+="+ "
                elif j=='1':
                    str1+='x '
                elif j=='-1':
                    str1+='o '
                elif j=='2':
                    str1+='/ '
            str1+='\n'
        return str1
    def clear(self):
        '''
        clears the board
        '''
        l1=[]
        l2=[]
        for i in range(0,self.__row):
            for i in range(0,self.__col):
                l1.append('0')
            l2.append(l1)
            l1=[]
        self.__data=l2
    def findEmptySquare(self):
        '''
        finds a square with value 0 and returns its coordinates
        '''
        
        x=0
        y=0
        for i in self.__data:
            y+=1
            x=0
            for j in i:
                x+=1
                if j=='0':
                    return x,y
        '''
        ok=0
        while ok==0:
            x=randint(0,self.__col-1)
            y=randint(0,self.__row-1)   
            if self.__data[y][x]=='0':
                ok=1
            else:
                ok=0
        return x,y  
        ''' 
    def moveX(self,square):
        '''
        changes the value of a square to 1 and the value of its neighbors to 2
        '''
        x=square.getX()
        y=square.getY()
        if x>self.__col or y>self.__row:
            raise ValueError("square outside of the board!")
        if self.__data[y-1][x-1]=='0':
            self.__data[y-1][x-1]='1'
            if x-1!=0:
                self.__data[y-1][x-2]='2'
            if x-1!=self.__col-1:
                self.__data[y-1][x]='2'
            if y-1!=0:
                self.__data[y-2][x-1]='2'
                if x-1!=0:
                    self.__data[y-2][x-2]='2'
                if x-1!=self.__col-1:
                    self.__data[y-2][x]='2'
            if y-1!=self.__row-1:
                self.__data[y][x-1]='2'
                if x-1!=0:
                    self.__data[y][x-2]='2'
                if x-1!=self.__col-1:
                    self.__data[y][x]='2'
        else:
            raise ValueError("square already occupied!")
    def moveO(self,square):
        '''
        change the value of a square to -1 and the value of its neighbors to 2
        '''
        x=square.getX()
        y=square.getY()
        if x>self.__col or y>self.__row:
            raise ValueError("square outside of the board!")
        if self.__data[y-1][x-1]=='0':
            self.__data[y-1][x-1]='-1'
            if x-1!=0:
                self.__data[y-1][x-2]='2'
            if x-1!=self.__col-1:
                self.__data[y-1][x]='2'
            if y-1!=0:
                self.__data[y-2][x-1]='2'
                if x-1!=0:
                    self.__data[y-2][x-2]='2'
                if x-1!=self.__col-1:
                    self.__data[y-2][x]='2'
            if y-1!=self.__row-1:
                self.__data[y][x-1]='2'
                if x-1!=0:
                    self.__data[y][x-2]='2'
                if x-1!=self.__col-1:
                    self.__data[y][x]='2'
        else:
            raise ValueError("square already occupied!")
    def isGameWon(self):
        '''
        verifies if the board is full
        '''
        k=0
        for i in self.__data:
            for j in i:
                if j=='0':
                    k=1
        if k==0:
            return True
        else:
            return False