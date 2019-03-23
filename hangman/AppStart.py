'''
Created on 31 ian. 2018

@author: Catalin
'''
from Controller.Controller import Controller
from Repo.sentenceRepo import sentenceRepo
from UI.menu import UI

r=sentenceRepo()
r.addSentence("Anna has apples")
r.addSentence("John eats strawberries")

c=Controller(r)
u=UI(c)

u.main()