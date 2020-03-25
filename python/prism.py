# Title: Electric Potential Inside a Nested Prism
#Author: Lisa Carpenter

'''Abstract: This script models the potential surrounding a hollow, square box
of potential V = 1, with the potential set to 0 at distances far from the
center of the box.  The model makes use of the Jacobi method, which is a 
relaxation method for solving the 2nd order differential equation which 
describes the situation outlined above.  Laplace's equation allows us to 
relate the potential at a specific location to the potential of areas nearby.  
By using a matrix to represent the potential at locations in the xy plane, 
the Jacobi method is used to iterate the potential at every space until the 
solution ceases to change. A small dv is used and the dv for each location 
is checked against its neighbors.  When dv has dropped below a chosen epsilon 
value, the process is stopped and the potential is said to be relaxed. The 
potential is then displayed using a spectral map.'''

from pylab import *

# boundaries for the box in which the potential will be mapped
X = 100
Y = 100
# indeces on the edges of the matrix
xf = X - 1
yf = Y - 1
# prism length and width (even number)
P = 30
# initialize array to represent the potential in the xy plane
V = ones([X, Y], dtype = float)
# region outside of box set to random initial value, chosen here to be 0.5.  
for i in range (1, X):
    for j in range(1, Y):
        #only change points outside of the box
        if i < (X - P) / 2 or i >= (X + P) / 2 \
            or j < (Y - P) / 2 or j >= (Y + P) / 2:
            V[i, j] = 0.5
#S set the boundaries of the entire region to be 0.
V[0, :] = 0.0
V[:, 0] = 0.0
V[xf, :] = 0.0
V[:, yf] = 0.0
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

