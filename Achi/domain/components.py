'''
Created on 3 feb. 2018

@author: Catalin
'''
'''
class square():
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
'''
class board():
    '''
    board class
    '''
    def __init__(self):
        self.__data=[['0','0','0'],['0','0','0'],['0','0','0']]
    def __str__(self):
        s='+---+---+---+\n'
        for i in self.__data:
            s+='|'
            for j in i:
                if j=='0':
                    s+='   |'
                elif j=='1':
                    s+=' X |'
                elif j=='2':
                    s+=' O |'
            s+='\n'
            s+='+---+---+---+\n'
        return s
    def overrr(self,d):
        '''
        updates the data
        '''
        self.__data=d
    def getData(self):
        '''
        returns the data
        '''
        return self.__data
    def movX(self,i,j):
        '''
        program that moves x from one square to another
        '''
        if i>2 or j>2 or i<0 or j<0:
            raise ValueError("invalid coordinates")
        
        if self.__data[i][j]=='0':
            self.__data[i][j]='1'
        else:
            raise ValueError("square already occupied")
    def movO(self,i,j):
        '''
        program that moves 0 from one square to another
        '''
        if i>2 or j>2 or i<0 or j<0:
            raise ValueError("invalid coordinates")
        
        if self.__data[i][j]=='0':
            self.__data[i][j]='2'
        else:
            raise ValueError("square already occupied")
    def replaceX(self,i,j,i1,j1):
        '''
        program that moves x from one square to another
        input: i,j,i1,j1
        '''
        if self.__data[i][j]=='1' and self.__data[i1][j1]=='0' and ((i==i1 or i==i1-1 or i==i1+1) and (j==j1 or j==j1-1 or j==j1+1)):
            self.__data[i1][j1]='1'
            self.__data[i][j]='0'
        else:
            raise ValueError("error")
    def replaceO(self,i,j,i1,j1):
        '''
        program that moves o from one square to another
        input: i,j,i1,j1
        '''
        if self.__data[i][j]=='2' and self.__data[i1][j1]=='0':
            self.__data[i1][j1]='2'
            self.__data[i][j]='0'
        else:
            raise ValueError("error")
    
    def dont(self):
        ok=0
        for i in range(0,3):
            if self.__data[i]==['1','1','0']:
                self.__data[i]=['1','1','2']
                ok=1
            elif self.__data[i]==['0','1','1']:
                self.__data[i]=['2','1','1']
                ok=1
            if self.__data[i]==['1','0','1']:
                self.__data[i]=['1','2','1']
                ok=1
        if ok==0:
            if self.__data[0][0]=='1' and self.__data[1][1]=='1' and self.__data[2][2]=='0':
                self.__data[2][2]='2'
                ok=1
            elif self.__data[0][0]=='1' and self.__data[1][1]=='0' and self.__data[2][2]=='1':
                self.__data[1][1]='2'
                ok=1
            elif self.__data[0][0]=='0' and self.__data[1][1]=='1' and self.__data[2][2]=='1':
                self.__data[0][0]='2'
                ok=1
            elif self.__data[0][2]=='1' and self.__data[1][1]=='1' and self.__data[2][0]=='0':
                self.__data[2][0]='2'
                ok=1
            elif self.__data[0][2]=='1' and self.__data[1][1]=='0' and self.__data[2][0]=='1':
                self.__data[1][1]='2'
                ok=1
            elif self.__data[0][2]=='0' and self.__data[1][1]=='1' and self.__data[2][0]=='1':
                self.__data[0][2]='2'
                ok=1
            elif self.__data[0][0]=='0' and self.__data[1][0]=='1' and self.__data[2][0]=='1':
                self.__data[0][0]='2'
                ok=1
            elif self.__data[0][0]=='1' and self.__data[1][0]=='0' and self.__data[2][0]=='1':
                self.__data[1][0]='2'
                ok=1
            elif self.__data[0][0]=='1' and self.__data[1][0]=='1' and self.__data[2][0]=='0':
                self.__data[2][0]='2'
                ok=1
            elif self.__data[0][1]=='0' and self.__data[1][1]=='1' and self.__data[2][1]=='1':
                self.__data[0][1]='2'
            elif self.__data[0][1]=='1' and self.__data[1][1]=='0' and self.__data[2][1]=='1':
                self.__data[1][1]='2'
                ok=1
            elif self.__data[0][1]=='1' and self.__data[1][1]=='1' and self.__data[2][1]=='0':
                self.__data[2][1]='2'
                ok=1
            elif self.__data[0][2]=='1' and self.__data[1][2]=='1' and self.__data[2][2]=='0':
                self.__data[2][2]='2'
                ok=1
            elif self.__data[0][2]=='1' and self.__data[1][2]=='1' and self.__data[2][2]=='0':
                self.__data[0][2]='2'
                ok=1
            elif self.__data[0][2]=='1' and self.__data[1][2]=='0' and self.__data[2][2]=='1':
                self.__data[1][2]='2'
                ok=1
            elif self.__data[0][2]=='0' and self.__data[1][2]=='1' and self.__data[2][2]=='1':
                self.__data[0][2]='2'
                ok=1
            if ok==0:
                ok=0
                for i in range(0,3):
                    for j in range(0,3):
                        if self.__data[i][j]=='0':
                            self.__data[i][j]='2'
                            ok=1
                        if ok==1:
                            ok=2
                            break
                    if ok==2:
                        break
                
                        
    
    def findEmpty(self):
        '''
        program that finds an empty square and replaces it with O
        '''
        ok=0
        for i in range(0,3):
            for j in range(0,3):
                if self.__data[i][j]=='0':
                    self.__data[i][j]='2'
                    ok=1
                if ok==1:
                    ok=2
                    break
            if ok==2:
                break
            
    def findO(self):
        '''
        program that finds an O square
        output: i,j
        '''
        ok=0
        for i in range(0,3):
            for j in range(0,3):
                if self.__data[i][j]=='2':
                    return i,j
    
    def findE(self):
        '''
        program that finds an empty square
        output: i,j
        '''
        ok=0
        for i in range(0,3):
            for j in range(0,3):
                if self.__data[i][j]=='0':
                    return i,j
    def isgamewon(self):
        '''
        program that verifies if the game is won
        output: True or False
        '''
        if self.__data[0]==['1','1','1'] or self.__data[0]==['2','2','2']:
            return True
        elif self.__data[1]==['1','1','1'] or self.__data[0]==['2','2','2']:
            return True
        elif self.__data[2]==['1','1','1'] or self.__data[0]==['2','2','2']:
            return True
        elif self.__data[0][0]=='1' and self.__data[1][1]=='1' and self.__data[2][2]=='1':
            return True
        elif self.__data[0][0]=='2' and self.__data[1][1]=='2' and self.__data[2][2]=='2':
            return True
        elif self.__data[0][2]=='1' and self.__data[1][1]=='1' and self.__data[2][0]=='1':
            return True
        elif self.__data[0][2]=='2' and self.__data[1][1]=='2' and self.__data[2][0]=='2':
            return True
        elif self.__data[0][0]=='1' and self.__data[0][1]=='1' and self.__data[0][2]=='1':
            return True 
        elif self.__data[1][0]=='1' and self.__data[1][1]=='1' and self.__data[1][2]=='1':
            return True    
        elif self.__data[0][0]=='2' and self.__data[0][1]=='2' and self.__data[0][2]=='2':
            return True    
        elif self.__data[1][0]=='2' and self.__data[1][1]=='2' and self.__data[1][2]=='2':
            return True   
        elif self.__data[2][0]=='2' and self.__data[2][1]=='2' and self.__data[2][2]=='2':
            return True    
        elif self.__data[2][0]=='1' and self.__data[2][1]=='1' and self.__data[2][2]=='1':
            return True             

def tests():
    '''
    test function for board class
    '''
    b=board()
    assert b.getData()==[['0','0','0'],['0','0','0'],['0','0','0']]
    b.movX(1,1)
    assert b.getData()==[['0','0','0'],['0','1','0'],['0','0','0']]
    b.movO(2,2)
    assert b.getData()==[['0','0','0'],['0','1','0'],['0','0','2']]
    b.replaceX(1, 1, 0, 0)
    assert b.getData()==[['1','0','0'],['0','0','0'],['0','0','2']]
    b.replaceO(2, 2, 1, 1)
    assert b.getData()==[['1','0','0'],['0','2','0'],['0','0','0']]
    b.movX(0, 1)
    b.movX(0, 2)
    assert b.isgamewon()==True
    
tests()