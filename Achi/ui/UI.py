'''
Created on 3 feb. 2018

@author: Catalin
'''
class UI():
    '''
    user interface class
    '''
    def __init__(self,ctr):
        '''
        constructor for ui class
        '''
        self.__ctr=ctr
        
    def main(self):
        '''
        main programm
        '''
        keepAlive=True
        k=0
        while keepAlive:
            ok=0
            print(self.__ctr.printBoard())
            if k<4:
                print("place:")
                i,j=UI.readCoord()
                try:
                    self.__ctr.movX(i,j)
                    print(self.__ctr.printBoard())
                    k=k+1
                    ok=1
                    if self.__ctr.gw()==True:
                        print("you won")
                        #print(self.__ctr.printBoard())
                        break
                except ValueError as ve:
                    print(ve)
                if ok==1 and k==1:
                    self.__ctr.fnd()
                    if self.__ctr.gw()==True:
                        print("you lost")
                        break
                elif ok==1 and k>1:
                    try:
                        #self.__ctr.fnd()
                        self.__ctr.dont()
                        if self.__ctr.gw()==True:
                            print("you lost")
                            print(self.__ctr.printBoard())
                            break
                    except ValueError:
                        self.__ctr.fnd()
            elif k==4:
                print("move:")
                i,j,i1,j1=UI.readDC()
                try:
                    self.__ctr.replaceX(i,j,i1,j1)
                    print(self.__ctr.printBoard())
                    if self.__ctr.gw()==True:
                        print("you won")
                        #print(self.__ctr.printBoard())
                        break
                    ok=1
                except ValueError as ve:
                    print(ve)
                
                if ok==1:
                    self.__ctr.mmmO()
                    if self.__ctr.gw()==True:
                        print("you lost")
                        print(self.__ctr.printBoard())
                        break
                    
                    ok=0
                
                
    @staticmethod
    def readCoord():
        '''
        program that coord of a square
        output: i,j
        '''
        i=int(input("i:"))
        j=int(input("j:"))
        return i,j
    @staticmethod
    def readDC():
        '''
        program that reads coord of 2 squears
        output i,j,i1,j2
        '''
        ok=0
        print("from:")
        while ok==0:
            i=int(input("i:"))
            j=int(input("j:"))
            if i<3 and j<3 and i>-1 and j>-1:
                ok=1
            else:
                print("invalid")
        ok=0
        print("to:")
        while ok==0:
            i1=int(input("i:"))
            j2=int(input("j:"))
            if i1<3 and j2<3 and i1>-1 and j2>-1:
                ok=1
            else:
                print("invalid")
        return i,j,i1,j2
            