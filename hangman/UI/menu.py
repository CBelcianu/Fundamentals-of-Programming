'''
Created on 31 ian. 2018

@author: Catalin
'''
class UI():
    def __init__(self,ctrl):
        self.__ctrl=ctrl
    @staticmethod
    def printMenu():
        print("\t 1.add sentence")
        print("\t 2.start game")
    
    def main(self):
        keepAlive=True
        while keepAlive:
            UI.printMenu()
            command=input("Enter comand").strip()
            if command=='1':
                s=UI.readSentence()
                if self.__ctrl.find(s)==False:
                    print("sentence already added!")
                else:
                    self.__ctrl.addSentence(s)
            elif command=='0':
                l=self.__ctrl.getAll()
                for i in l:
                    print(i)
            elif command=='2':
                s=self.__ctrl.randomSentence()
                h="hangman"
                k=0
                pozitii=[0]
                ok=0
                hangman=''
                contor=0
                while ok==0 and k!=7:
                    c,pozitii,contor=UI.printJmk(s,pozitii)
                    print(c)
                    l=input("guess a letter:")
                    print("---------------------")
                    ceva=UI.findIn(s,l,pozitii)
                    if ceva!=False:
                        pozitii=ceva
                    else:
                        hangman+=h[k]
                        k=k+1
                    if contor==False:
                        hangman+=h[k]
                        k=k+1
                    print(hangman + '\n')
                    if k==7:
                        print("You lost!")
                        keepAlive=False
                        print(pozitii)
                    if contor==1:
                        print("Bine ba")
                        keepAlive=False
                    
    @staticmethod
    def findIn(s,l,k):
        ok=0
        g=0
        for i in range(0,len(s)):
            if s[i].lower()==l.lower():
                for x in k:
                    if x==i:
                        g=1
                if g==0:
                    k.append(i)
                    ok=1
        if ok==0:
            return False
        else:
            return k
                
    @staticmethod
    def readSentence():
        s=input("enter sentence:")
        return s
    @staticmethod
    def printJmk(s,pz):
        f=s[0].lower()
        l=s[len(s)-1].lower()
        c=''
        g1=0
        g2=0
        middle=[f]
        liniuta=0
        for i in range(0,len(s)):
            
            for x in pz:
                if x==i and i!=0:
                    c+=s[i]
                    g1=1
            
            for x in middle:
                if x==s[i]:
                    c+=s[i]
                    g2=1
                    #pz.append(i)
                    
            
                #if x==l:
                    #g2=1
                    #pz.append(i)
                    
            if g1==0 and g2==0:
                if s[i].lower()==f:
                    c+=f
                    pz.append(i)
                elif s[i].lower()==l:
                    c+=l
                    pz.append(i)
                elif s[i+1]==" " and s[i].lower()!=l and s[i].lower()!=f:
                    c+=s[i]
                    #pz.append(i)
                    middle.append(s[i])
                elif s[i-1]==" "and s[i].lower()!=l and s[i].lower()!=f:
                    c+=s[i]
                    #pz.append(i)
                    middle.append(s[i])
                elif s[i]==" ":
                    c+=' '
                    #pz.append(i)
                else:
                    c+='_'
                    liniuta+=1
                    '''
                for x in middle:
                    if x==l:
                        pz.append(i)
                        pz.append(i)
                        #break
                    '''
            if g2==1:
                liniuta=False        
            g1=0
            g2=0
        return c,pz,liniuta
                
                