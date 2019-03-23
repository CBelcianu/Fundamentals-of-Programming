'''
Created on 6 nov. 2017

@author: Catalin
'''
from math import sqrt

class Complex:
    '''
    Instances of this class represent complex numbers in the form z = a + bi
    '''
    
    def __init__(self, real, imag=0):
        """
        Constructor for Complex class
        Input: real,imag - real and imaginary parts, respectively
        """
        self.__real = real
        self.__imag = imag

    def modulus(self):
        return sqrt(self.__real ** 2 + self.__imag ** 2)

    def __add__(self, z):
        """
        Overload of the + operator that works with Complex and int parameters
        Input: z - number to add current with
        Output: The Complex number representing the sum
        Raises: TypeError if addition cannot be performed due to operator types
        """
        if isinstance(z, Complex):
            return Complex(self.__real + z.__real, self.__imag + z.__imag)
        if isinstance(z, int):
            return Complex(self.__real + z, self.__imag)
        raise TypeError("Invalid type for addition")

    def __mul__(self, z):
        """
        Overload of the * operator that works with Complex and int parameters
        Input: z - number to multiply current with
        Output: The Complex number representing the product
        Raises: TypeError if multiplication cannot be performed due to operator types
        """
        if isinstance(z, Complex):
            return Complex(self.__real * z.__real - self.__imag * z.__imag, self.__imag * z.__real + self.__real * z.__imag)
        if isinstance(z, int):
            return Complex(self.__real * z, self.__imag * z)
        raise TypeError("Not a complex number")

    def __eq__(self, z):
        """
        Overload the == operator
        Returns True iif the parameters represent the same complex number value
        """
        return self.__real == z.__real and self.__imag == z.__imag
   
    def getReal(self):
        """
        Getter for real part of complex number
        Output: The real part of number
        """
        return self.__real

    def getImag(self):
        return self.__imag

    def setReal(self, x):
        self.__real = x

    def setImag(self, y):
        self.__imag = y

    def __str__(self):
        r = ''
        if self.__real != 0:
            r += str(self.__real)
        if self.__real != 0 and self.__imag > 0:
            r += '+'
        if self.__imag != 0:
            if self.__imag == 1:
                r += 'i'
            elif self.__imag == -1:
                r += '-i'
            else:
                r += str(self.__imag) + 'i'
        return r

def test_complex():
    # 1,i,4i,-i,-3i,1+3i,-2+3i,2-5i,-2-i
    assert str(Complex(1)) == '1'
    assert str(Complex(0, 1)) == 'i'
    assert str(Complex(0, 4)) == '4i'
    assert str(Complex(0, -1)) == '-i'
    assert str(Complex(0, -3)) == '-3i'
    assert str(Complex(1, 3)) == '1+3i'
    assert str(Complex(-2, 3)) == '-2+3i'
    assert str(Complex(2, -5)) == '2-5i'
    assert str(Complex(-2, -1)) == '-2-i'

    x = Complex(2, -1)
    y = Complex(1, 3)
    z = x + y
    assert str(z) == '3+2i'
    z = x + y + y + y
    assert str(z) == '5+8i'
    assert str(x * y) == '5+5i'

    y = Complex(2, -1)
    assert x == y