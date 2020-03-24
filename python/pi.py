# Title: Computing Pi Using Archimedes' Method
# File: pi.py
# Author: Lisa Carpenter

# Abstract:  This program computes the value of pi to within 3 decimal
# places.  The method used will be to calculate the perimeters of two polygons,
# one polygon circumscribed about the circle and the other inscribed in the circle.  
# The number of sides on the two polygons is increased until the difference between 
# the two values is less than 1.0E-4, giving a lower and upper bound for pi. A list 
# of values will be generated as well, using the % function to ensure consistency and 
# equal column widths. 

import math

# define the maximum error in approximating pi
# start with a 3-sided polygon
eps = 0.0001
n = 3

# the upper and lower bounds of pi, respectively
piUpper = 1
piLower = 0

# initialize columns for output table 
listSides=[]
listPiLower=[]
listPiUpper=[]

while abs(piUpper - piLower) >= eps:
    theta = 360.0/n
    piLower = n * math.sin(math.radians(theta/2.0))
    piUpper = n * math.tan(math.radians(theta/2.0))
    listSides.append(n)
    listPiLower.append(piLower)
    listPiUpper.append(piUpper)
    n += 1

#print the headers on the list
print('%8s\t%16s\t%16s\t' % ('# Sides','Lower Bound','Upper Bound'))
numValues = len(listSides)

# print every 10th element on the list by using mod 10 and formatting for 
# column width, precision, and tabs.
for i in range(numValues):
    if i % (math.ceil(listSides[-1]/10)) == 0:
        print('%8d\t%16.5f\t%16.5f\t' % (listSides[i],listPiLower[i],listPiUpper[i]))        


