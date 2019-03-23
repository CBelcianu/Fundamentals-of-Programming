'''
Created on 9 ian. 2018

@author: Catalin
'''
def readBoardSize():
    '''
    reads the number of rows and columns of the board and returns them
    '''
    print("provide the board size")
    ok1=0
    ok2=0
    while ok1==0:
        x=int(input("number of rows:"))
        if x>9:
            print("the number of rows should be less than 10")
        elif x<4:
            print("the number of rows should be more than 4")
        else:
            ok1=1
    while ok2==0:
        y=int(input("number of columns:"))
        if y>9:
            print("the number of columns should be less than 10")
        elif y<4:
            print("the number of columns should be more than 4")
        else:
            ok2=1
    return x,y