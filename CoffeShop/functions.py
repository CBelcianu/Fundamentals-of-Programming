'''
Created on 14 nov. 2017

@author: Catalin
'''
def isNumber(x):
    for i in range(0,len(x)):
        if(x[i]!='0' and x[i]!='1' and x[i]!='2' and x[i]!='3' and x[i]!='4' and x[i]!='5' and x[i]!='6' and x[i]!='7' and x[i]!='8' and x[i]!='9' and x[i]!='.'):
            return False
    return True

def add(cl,params):
    if(len(params)==3):
        cl.append([params[0],params[1],float(params[2])])
    else:
        raise ValueError("Invalid syntax!")
    
def listc(cl,params):
    if(len(params)==0):
        for i in cl:
            print(i)
            
def filterc(cl,params):
    k=0
    if len(params)==2:
        for i in cl:
            if i[1]==params[0] and i[2]<float(params[1]):
                print(i)
                k=1
    elif len(params)==1 and isNumber(params[0])==True:
        for i in cl:
            if float(i[2])<float(params[0]):
                print(i)
                k=1
    elif len(params)==1 and isNumber(params[0])==False:
        for i in cl:
            if i[1]==params[0]:
                print(i)
                k=1
    elif len(params)==0:
        raise ValueError("invalid syntax")
    if(k==0):
        raise ValueError("no such coffees!!")
    
def nrCoffes(cl,params):
    s=0
    if len(params)==1:
        for i in cl:
            if i[1]==params[0]:
                s=s+1
    else:
        raise ValueError("invalid syntax!")
    return s

def delete(cl,params):
    i=0
    if len(params)==1:
        while i<len(cl):
            if cl[i][1]==params[0]:
                cl.pop(i)
                i-=1
            i+=1
    else:
        raise ValueError("is!")