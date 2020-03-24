# -*- coding: utf-8 -*-
#Assignment: 02
#Question: 2: The Pyrochlore Lattice
#Author: Lisa Carpenter
#Date: September 13, 2011

#Abstract:  This program will originate a plot showing the structure of the
#Pyrochlore Lattice. This is done by defining a set of arrays representing
#different basis vectore for both position in the coordinate system and
#position of the four atoms at each position.  While the points are being
#generating by iterating through nested for loops, the points are being added
#to a 500*3 dimensional array.  The array will then be used to plot all of the
#atom positions in scatterplots showing views from the xy, yz, and zx planes.
#The data will also be written to a pyrochlore.dat file.  

from pylab import *

#setting a = 1 Angstrom
a = 1.0

#defining the numpy arrays for the vector position basis from the origin
a_1 = array([0.0,a/2.0,a/2.0])
a_2 = array([a/2.0,0.0,a/2.0])
a_3 = array([a/2.0,a/2.0,0.0])

#defining the numpy arrays for the atom position basis on each lattic corner
r_1 = array([0.0,0.0,0.0])
r_2 = array([a/4.0,a/4.0,0])
r_3 = array([a/4.0,0.0,a/4.0])
r_4 = array([0.0,a/4.0,a/4.0])

#defining the array to iterate through for each atom's position on the lattice
basisAtom = array([r_1,r_2,r_3,r_4])

#the atom position will be defined by three coordinates.  An array will collect
#the data, row by row for 500 rows.  The counter for the rows will start at 0,
#indexing the first row.  
atomPosition = zeros([500,3])
p = 0
#Writing a file named pyrochlore.dat to list the coordinates of 500+ atoms
#filename = "pyrochlore.dat"
#Opening the file and making it writable
#file = open(filename,"wb")

#Creating a for loop that will move along each point in a 3d, 5*5*5
#coordinate system

for x in range (6):
    for y in range (6):
        for z in range (6):
#The basis vector is a linear superposition of each x, y, and z unit vector
            basisVec = x*a_1 + y*a_2 + z*a_3
#For each of these vectors, four atoms will be added one by one
            for b in range (4):
#The position of each atom is the sum of the basis vector and the basis atom
#vector as measured from the origin.  
                if p < 500:
                    atomPosition[p] = basisVec + basisAtom[b]
#The atom position is stored as a row in the atomPosition array and the
#row index is increased by one for the next iteration.  
                p = p + 1

#writing the atom position to a file called pyrochlore.dat
savetxt('pyrochlore.dat', atomPosition, fmt = '%8.4d')

#the color must iterate through 4 different colors, representing each of the
#four atom positions.
#Each figure is given an x and y label displaying proper units and a title
color = ['r','b','g','y']
#number each of the three figures
figure(1)
ylabel('y-axis (1.0E-10 meters)')
xlabel('x-axis (1.0E-10 meters)')
title('X versus Y Scatterplot for Pyrochlore Lattice')
#plotting each point from the 500 data points
#changing the color in sets of four
for n in range(500):
    for k in range (0,3):
        scatter(atomPosition[n,0],atomPosition[n,1],s = 2,c = color[k])
        
#repeating for figure 2        
figure(2)
ylabel('z-axis (1.0E-10 meters)')
xlabel('y-axis (1.0E-10 meters)')
title('Y versus Z Scatterplot for Pyrochlore Lattice')
for n in range(500):
    for k in range (0,3):
        scatter(atomPosition[n,1],atomPosition[n,2],s = 2,c = color[k])
        
#repeating for figure 3       
figure(3)
ylabel('x-axis (1.0E-10 meters)')
xlabel('z-axis (1.0E-10 meters)')
title('Z versus X Scatterplot for Pyrochlore Lattice')
for n in range (500):
    for k in range (0,3):
        scatter(atomPosition[n,2],atomPosition[n,0],s = 2,c = color[k])
        
#show the figures
show()


            
           
            
            


