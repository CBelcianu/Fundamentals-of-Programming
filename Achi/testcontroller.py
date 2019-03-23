'''
Created on 3 feb. 2018

@author: Catalin
'''
from controller.controller import controller
from domain.components import board
def tests():
    '''
    test function for controller class
    '''
    b=board
    c=controller(b)
    c.movX(1,1)
    assert b.getData()==[['0','0','0'],['0','1','0'],['0','0','0']]
    c.movO(2,2)
    assert b.getData()==[['0','0','0'],['0','1','0'],['0','0','2']]
    c.replaceX(1, 1, 0, 0)
    assert b.getData()==[['1','0','0'],['0','0','0'],['0','0','2']]
    c.replaceO(2, 2, 1, 1)
    assert b.getData()==[['1','0','0'],['0','2','0'],['0','0','0']]
    c.movX(0, 1)
    c.movX(0, 2)
    assert c.gw()==True
tests()