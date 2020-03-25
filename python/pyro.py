# -*- coding: utf-8 -*-
#Assignment: 02
#Question: 2: The Pyrochlore Lattice
#Author: Lisa Carpenter
#Date: September 13, 2011

'''Abstract:  This script models the structure of the Pyrochlore Lattice. 
This is done by defining a set of arrays representing basis vectors for both 
position in the coordinate system and position of the four atoms at each 
position.  While the points are generated, they are added to a 500*3 dimensional 
array.  The array is used to plot all of the atom positions in scatterplots 
showing views from the xy, yz, and zx planes.The data is written to a pyrochlore.dat 
file.'''

from pylab import *

# 1 Angstrom
a = 1.0

# vector position basis from the origin
a_1 = array([0.0, a/2.0, a/2.0])
a_2 = array([a/2.0, 0.0, a/2.0])
a_3 = array([a/2.0, a/2.0, 0.0])

# atom position basis on each lattice corner
r_1 = array([0.0, 0.0, 0.0])
r_2 = array([a/4.0, a/4.0, 0])
r_3 = array([a/4.0, 0.0, a/4.0])
r_4 = array([0.0, a/4.0, a/4.0])

basisAtom = array([r_1, r_2, r_3, r_4])

atomPosition = zeros([500,3])
p = 0

for x in range (6):
    for y in range (6):
        for z in range (6):
            # linear superposition of each x, y, and z unit vector
            basisVec = x*a_1 + y*a_2 + z*a_3
            # add four atoms
            for b in range (4):
                if p < 500:
                    atomPosition[p] = basisVec + basisAtom[b]
                p = p + 1

savetxt('pyrochlore.dat', atomPosition, fmt = '%8.4d')

color = ['r','b','g','y']
figure(1)
ylabel('y-axis (1.0E-10 meters)')
xlabel('x-axis (1.0E-10 meters)')
title('X versus Y Scatterplot for Pyrochlore Lattice')
for n in range(500):
    for k in range (0,3):
        scatter(atomPosition[n,0],atomPosition[n,1],s = 2,color = color[k])

figure(2)
ylabel('z-axis (1.0E-10 meters)')
xlabel('y-axis (1.0E-10 meters)')
title('Y versus Z Scatterplot for Pyrochlore Lattice')
for n in range(500):
    for k in range (0,3):
        scatter(atomPosition[n,1],atomPosition[n,2],s = 2,color = color[k])

figure(3)
ylabel('x-axis (1.0E-10 meters)')
xlabel('z-axis (1.0E-10 meters)')
title('Z versus X Scatterplot for Pyrochlore Lattice')
for n in range (500):
    for k in range (0,3):
        scatter(atomPosition[n,2],atomPosition[n,0],s = 2,color = color[k])
        
show()
