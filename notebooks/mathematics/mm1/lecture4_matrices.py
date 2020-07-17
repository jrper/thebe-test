#!/usr/bin/env python 

## Maths Methods 1
## Lecture 4 (Matrices)

## In this file, variable names use the following prefix convention:
## 's' (e.g. sDotProduct) means the variable is a scalar
## 'v' (e.g. vCrossProduct) means the variable is a vector
## 'm' (e.g. mA) means the variable is a matrix

import numpy
import pylab
from math import pi

###### DEFINING A MATRIX ######
###### Lecture 4, slide 3 ######
# Define matrices in Python using numpy.matrix

# mA is a SQUARE matrix
mA = numpy.matrix([[2, 3, -4],
                   [3, -1, 2],
                   [4, 2, 2]])   
# mB is a NON-SQUARE matrix
mB = numpy.matrix([[2, -4, 1, -2],
                   [7, 8, 0, 3]])   
                  
# REMEMBER: when stating the dimension of a matrix (e.g. 3 x 3, 2 x 4, etc)
# it's *R*ows Fi*R*st, *C*olumns Se*C*ond.
# So, mA is 3 x 3 matrix, mB is a 2 x 4 matrix.

# You can also use numpy.shape to determine the dimension of a matrix
print "\nThe dimension of A is ", numpy.shape(mA)
print "\nThe dimension of B is ", numpy.shape(mB)


###### MATRIX-SCALAR MULTIPLICATION ######
###### Lecture 4, slide 5 ######
mD = numpy.matrix([[2, -4, 1, -2],
                   [7, 8, 0, 3]])  
         
print "\n3*D = ", 3*mD


###### MATRIX ADDITION AND SUBTRACTION ######
###### Lecture 4, slide 6, 7 ######
mE = numpy.matrix([[2, -4],
                   [7, 8]])
                  
mF = numpy.matrix([[4, 0],
                   [2, -1]])
         
print "\nE + F = ", mE + mF

print "\nE - F = ", mE - mF

# NOTE: The two matrices must have the same dimension. If they do not,
# Python will give an error. Try adding mE (2 x 2) and mB (2 x 4). Python will give: 
# ValueError: operands could not be broadcast together with shapes (2,2) (2,4)


###### MATRIX-MATRIX MULTIPLICATION ######
###### Lecture 4, slide 10 ######
mE = numpy.matrix([[2, -4],
                   [7, 8],
                   [3, 2]])  
mH = numpy.matrix([[4, 0, 0, 1],
                   [2, -1, 3, -2]])                  
         
print "\nE*H = ", mE*mH


###### MATRIX TRANSPOSE ######
###### Lecture 4, slide 12, 13 ######
# Non-square matrix
mB = numpy.matrix([[2, -4],
                   [7, 8],
                   [3, 2]])
                  
mB_transpose = numpy.transpose(mB)
print "\nThe transpose of (non-square) B = ", mB_transpose

# Square matrix
mB = numpy.matrix([[2, 3, -4],
                   [3, -1, 2],
                   [4, 2, 2]])                 

mB_transpose = numpy.transpose(mB)
print "\nThe transpose of (square) B = ", mB_transpose


###### IDENTITY MATRIX ######
###### Lecture 4, slide 15 ######
mI = numpy.identity(3) # Creates a 3 x 3 identity matrix
mB = numpy.matrix([[2, 3, -4],
                   [3, -1, 2],
                   [4, 2, 2]])                 

# mIB should be equal to mB
mIB = mI*mB
print "\nI*B = ", mIB


###### DETERMINANTS ######
###### Lecture 4, slide 16 ######
# 2 x 2 example
mD = numpy.matrix([[1, 4],
                   [-3, 5]])            
sDet = numpy.linalg.det(mD)
print "\ndet(D) = %f" % sDet

# 3 x 3 example
mA = numpy.matrix([[1, 2, 4],
                   [-3, 1, -2],
                   [3, 2, 5]])   
det = numpy.linalg.det(mA)
print "\ndet(A) = %f" % sDet

