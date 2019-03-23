'''
Created on 20 dec. 2017

@author: Catalin
'''
from repo.fileRepo import fileRepo
from op.controller import controller
from UI.UI import ui

rep=fileRepo()
ctr=controller(rep)
u=ui(ctr)

u.main()