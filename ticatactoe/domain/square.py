'''
Created on 6 dec. 2017

@author: Catalin
'''
class square:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    
class board:
    def __init__(self):
        self.__data=[['0','0','0'],['0','0','0'],['0','0','0']]
    def __str__(self):
        str1='\n'
        r=0
        l=0
        for i in self.__data:
            r+=1
            l=0
            for j in i:
                l+=1
                str1+=' '
                if j=='1':
                    str1+='X'
                elif j=='-1':
                    str1+='O'
                elif j=='0':
                    str1+=' '
                if(l!=3):
                    str1+=' '
                    str1+='|'
            if(r!=3):
                str1+='\n'
                str1+='-----------'
                str1+='\n'
        return str1  
    def moveX(self,square): 
        x=square.getX()
        y=square.getY()
        if x>3 or y>3:
            raise ValueError("square outside of the board!")
        if self.__data[y-1][x-1]=='0':
            self.__data[y-1][x-1]='1'
        else:
            raise ValueError("square already occupied!")
    def moveO(self,square):
        x=square.getX()
        y=square.getY()
        if x>3 or y>3:
            raise ValueError("square outside of the board!")
        if self.__data[y-1][x-1]=='0':
            self.__data[y-1][x-1]='-1'
        else:
            raise ValueError("square already occupied")
    def isGameWon(self):
        s=''
        if self.__data[0]==['1','1','1'] or self.__data[1]==['1','1','1'] or self.__data[2]==['1','1','1']:
            s="You won"
        elif self.__data[0][0]=='1' and self.__data[1][1]=='1' and self.__data[2][2]=='1' or self.__data[2][0]=='1' and self.__data[1][1]=='1' and self.__data[0][2]=='1':
            s="you won"
        elif self.__data[0][0]=='1' and self.__data[1][0]=='1' and self.__data[2][0]=='1' or self.__data[0][1]=='1' and self.__data[1][1]=='1' and self.__data[2][1]=='1' or self.__data[0][2]=='1' and self.__data[1][2]=='1' and self.__data[2][2]=='1':
            s="you won"
        elif self.__data[0]==['-1','-1','-1'] or self.__data[1]==['-1','-1','-1'] or self.__data[2]==['-1','-1','-1']:
            s="Game is won"
        elif self.__data[0][0]=='-1' and self.__data[1][1]=='-1' and self.__data[2][2]=='-1' or self.__data[2][0]=='-1' and self.__data[1][1]=='-1' and self.__data[0][2]=='-1':
            s="Game is won"
        elif self.__data[0][0]=='-1' and self.__data[1][0]=='-1' and self.__data[2][0]=='-1' or self.__data[0][1]=='-1' and self.__data[1][1]=='-1' and self.__data[2][1]=='-1' or self.__data[0][2]=='-1' and self.__data[1][2]=='-1' and self.__data[2][2]=='-1':
            s="Game is won won"
        return(s)
               
x=board()
print(str(x))
x.moveX(square(1,1))
print(str(x))
x.moveO(square(2,1))
print(str(x))
x.moveO(square(2,2))
print(str(x))
x.moveX(square(1,2))
print(str(x))
x.moveO(square(2,3))
print(str(x))
print(x.isGameWon())