'''
Created on 14 nov. 2017

@author: Catalin
'''
from functions import *
def readCommand():
    x=input(">>").split()
    cmd=x[0]
    params=x[1:]
    return cmd,params

def testInIt(cl):
    cl.append(["Latte-Machiato","Italy",7.9])
    cl.append(["Starbucks","USA",9])
    cl.append(["Lavazza","Italy",8.9])
    cl.append(["La-Festa","France",6.7])

def main():
    cl=[]
    testInIt(cl)
    while True:
        cmd,params=readCommand()
        if cmd == "add":
            try:
                add(cl,params)
            except ValueError as ve:
                print(ve)
        elif cmd == "list":
            listc(cl,params)
        elif cmd == "filter":
            try:
                filterc(cl, params)
            except ValueError as ve:
                print(ve)
        elif cmd == "delete":
            try:
                n=nrCoffes(cl, params)
                print("there are",n,"coffees from",params[0],"!Do you want to procede? yes/no")
                cmd1=input()
                if cmd1=="yes":
                    try:
                        delete(cl, params)
                    except ValueError as ve:
                        print(ve)
                elif cmd1=="no":
                    pass
                else:
                    print("Invalid command!")
            except ValueError as ve:
                print(ve)

main()