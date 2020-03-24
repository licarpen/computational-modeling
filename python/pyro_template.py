# -*- coding: utf-8 -*-
#Assignment: 02
#Question: 2: The Pyrochlore Lattice
#Author: Lisa Carpenter
#Date: September 13, 2011

#Abstract:  This program will originate a plot showing the structure of the
#Pyrochlore Lattice.

from pylab import *

#setting a = 1 Angstrom
a = 1.0E-10

#defining the numpy arrays for the vector position basis from the origin
a_1 = array([0,a/2,a/2])
a_2 = array([a/2,0,a/2])
a_3 = array([a/2,a/2,0])

#defining the numpy arrays for the atom position basis on each lattic corner
r_1 = array([0,0,0])
r_2 = array([a/4,a/4,0])
r_3 = array([a/4,0,a/4])
r_4 = array([0,a/4,a/4])

#defining the array to iterate through for each atom's position on the lattice
basisAtom = ([r_1,r_2,r_3,r_4])

#the atom position will be defined by three coordinates.  Here it is set to take
#One value, which will be an array of three values.  
atomPosition = [0]

#Writing a file named pyrochlore.dat to list the coordinates of 500+ atoms
filename = "pyrochlore.dat"
#Opening the file and making it writable
file = open(filename,"wb")

#Creating a for loop that will move along each point in a 3d, 5*5*5
#coordinate system
for x in range (-5,5):
    for y in range (-5,5):
        for z in range (-5,5):
#The basis vector is a linear superposition of each x, y, and z unit vector
            basisVec = x*a_1 + y*a_2 + z*a_3
#For each of these vectors, four atoms will be added one by one
            for b in range (0,3):
                i = 0
#The position of each atom is the sum of the basis vector and the basis atom
#vector as measured from the origin.  
                atomPosition[i] = basisVec + basisAtom[b]
                i += 1
#In order to write to a file, a convert each atom's coordinates to a string
#and strip the brackets for style
                aPos1 = atomPosition[:]
                aPos2 = str(atomPosition).strip('array([])')
#now that my coordinates are a string, I can write them to a file
                file.write(aPos2)
#and separate the coordinates for each atom by lines.
                file.write("\n")


scatter(aPos1[:][0],aPos1[:][1])
pylab.show()


#Now I close the file.  
file.close()

            
           
            
            


