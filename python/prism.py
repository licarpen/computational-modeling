#Assignment Number: 04
#Question Number: 03: Electric Potential Inside a Nested Prism: G&N 5.1
#Author: Lisa Carpenter
#Date: 10.09.2011
#File Name: prism.py

'''Abstract: This program will show the potential surrounding a square box
of potential V = 1, with the potential set to 0 at distances far from the
center of the box.  This will be shown using a spectral diagram.  The  method
used to do this will be the Jacobi Method, which is a relaxation method for
solving the 2nd order differential equation which describes the situation
outlined above.  Laplace's equation allows us to relate the potential at a
specific location to the potential of areas nearby.  By using a matrix to
represent the potential at locations in the xy plane, the Jacobi method is used
to iterate the potential at every space until the solution ceases to change.
A small dv is used and the dv for each location is checked against its
neighbors.  When dv has dropped below a suitable chosen eps value, the process
is stopped and the potential is said to be relaxed.  The potential is then
shown using a specrtral map.  

'''
from pylab import *

#Set the boundaries for the box in which the potential will be mapped
X = 100
Y = 100
#Determine the indeces on the edges of the matrix
xf = X - 1
yf = Y - 1
#Set prism length and width to an even number
P = 30
#Create an array to represent the potential in the xy plane.  Set all entries
#to 1
V = ones([X,Y], dtype = float)
#Use a for loop to set region outside of the box to a random initial value,
#chosen here to be 0.5.  
for i in range (1,X):
    for j in range(1,Y):
#Only change points outside of the box
            if i < (X - P)/2 or i >= (X + P)/2 \
               or j < (Y - P)/2 or j >= (Y + P)/2:
                V[i,j] = 0.5
#Set the boundaries of the entire region to be 0.
V[0,:] = 0.0
V[:,0] = 0.0
V[xf,:] = 0.0
V[:,yf] = 0.0
#Choose a small value for epsilon (eps)
eps = 0.05
#Initialize dv to some number greater than 0.
dv = 1.0
#Enter while loop to relax the potential until chosen eps is reached for
#every entry in the V matrix.  
while dv > eps:
#Maintain a potential of 0 at the boundaries
    for i in range (1,xf):
        for j in range(1,yf):
#Maintain a potential of 1 inside the box
            if i < (X - P)/2 or i >= (X + P)/2 or \
               j < (Y - P)/2 or j >= (Y + P)/2:
#Initialize dv to 0
                dv = 0.0
#Relax potential
                V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])
#Calculate dv to determine if eps has been reached
                dv = abs(V[i,j] - V[i+1,j+1])
#Show the data on a spectral map with a colorbar and title
title('Potential for a Hollow Metallic Prism Using Jacobi Relaxation Method')
xlabel('x')
ylabel('y')
#Label the potential at center and boundaries
text(45,50,'V = 1')
text(35,8, 'V = 0 at boundaries')
imshow(V,cmap=cm.spectral)
colorbar()
show()

