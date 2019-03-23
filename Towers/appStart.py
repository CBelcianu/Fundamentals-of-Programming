'''
Created on 1 feb. 2018

@author: Catalin
'''
from Repository.resRepo import resRepo,occupiedRooms,roomRepo
from Controller.resCtrl import resCtrl
from UI.UI import UI
from Domain.entities import Room,Reservation,date

res=resRepo()
free=roomRepo()
occ=occupiedRooms()

free.addRoom(Room(1,"family"))
free.addRoom(Room(2,"double"))
free.addRoom(Room(3,"single"))
free.addRoom(Room(4,"family"))
free.addRoom(Room(5,"double"))
free.addRoom(Room(6,"single"))
free.addRoom(Room(7,"family"))
free.addRoom(Room(8,"double"))
free.addRoom(Room(9,"single"))
free.addRoom(Room(10,"family"))

#res.addRes(Reservation(1234,1,"Pop",3,date('09','05'),date('10','25')))

ctrl=resCtrl(res,free,occ)

ui=UI(ctrl)

ui.main()