'''
Created on 19 dec. 2017

@author: Catalin
'''
from op.controller import controller
from repo.repo import busRepo,routeRepo
from UI.UI import UI
from domain.entities import route,bus
rRepo=routeRepo()
bRepo=busRepo()
rRepo.add(route(1,20))
rRepo.add(route(2,20))
rRepo.add(route(3,20))
rRepo.add(route(4,20))
bRepo.add(bus(1,2,"Merc",5))
bRepo.add(bus(2,3,"Volv",6))
ctr=controller(rRepo,bRepo)
ui=UI(ctr)
ui.main()