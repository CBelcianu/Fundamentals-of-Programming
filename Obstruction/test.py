'''
Created on 9 ian. 2018

@author: Catalin
'''
import unittest
from domain.components import board,square

class Test(unittest.TestCase):
    def testSquare(self):
        s=square(3,4)
        self.assertEqual(s.getX(),3)
        self.assertEqual(s.getY(),4)
        
    def testBoard(self):
        b=board(4,4)
        self.assertEqual(b.getC(),4)
        self.assertEqual(b.getR(),4)
        b.moveX(square(4,4))
        self.assertEqual(b.getData(),[['0','0','0','0'],['0','0','0','0'],['0','0','2','2'],['0','0','2','1']])
        b.clear()
        self.assertEqual(b.getData(),[['0','0','0','0'],['0','0','0','0'],['0','0','0','0'],['0','0','0','0']])