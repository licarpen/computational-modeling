#Assignment Number: 04
#Question Number: 03: Electric Potential Inside a Nested Prism: G&N 5.1
#Author: Lisa Carpenter
#Date: 10.09.2011
#File Name: prism.py

#Abstract:

from pylab import *


numX = 100
numY = 100
#Set prism length and width to an even number
P = 6
V = ones([numX,numY], dtype = float)

for i in range (1,numX-2):
    for j in range(1,numY-2):
            if i > (numX -1 - P)/2 or i > (numX -1 + P)/2:
                if j < (numY -1 - P)/2 or j > (numY -1 + P)/2:
                    V[i,j] = 1.5


V[0,:] = 0.0
V[:,0] = 0.0
V[numX-1,:] = 0.0
V[:,numY-1] = 0.0
eps = 0.05
dv = 1.0
while dv > eps:
    for i in range (1,numX-2):
        for j in range(1,numY-2):
            if i < (numX -1 - P)/2 or i > (numX - 1 + P)/2:
                if j < (numY -1 - P)/2 or j > (numY -1 + P)/2:
                    dv = 0.0
                    V[i,j] = 1/4*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])
                    dv = abs(V[i,j] - V[i+1,j+1])
                    print dv
                    print V

inshow(V,cmap=cm.spectral)
show()

