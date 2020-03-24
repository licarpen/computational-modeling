# Title: Computing Pi Using Archimedes' Method
# File: pi.py
# Author: Lisa Carpenter

# Abstract:  This program computes the value of pi to within 3 decimal
# places.  The method used will be to calculate the perimeters of two polygons,
# one polygon circumscribed about the circle and the other inscribed in the circle.  
# The number of sides on the two polygons will be increased using a while loop.  
# When the difference between the two values is less than 1.0E-4, the value will be 
# used as an approximation for pi. A list of values will be generated as well, using 
# the % function to ensure consistency and equal column widths.  

from pylab import *

# define the maximum error in approximating pi
# start with a 3-sided polygon
errorMin = 0.0001
n = 3

# the upper and lower bounds of pi, respectively
pOut = 1
pIn = 0

# initialize columns for output table 
listSides=[]
listpIn=[]
listpOut=[]

#using a while loop to calculate the difference in the upper and lower bounds
#of the perimeters
while pOut - pIn >= errorMin:
#The outer perimeter is defined as n2Rtan(pi/n), where n is the number of sides
#pOut is the calculation of pi, taking the outer perimeter divided by 2R.
#The inner perimeter is defined as n2Rsin(pi/n), where n is the number of sides
#pIn is the lower bound on pi.  
#calculating pOut and pIn and entering data into the list
    pOut = n*tan(pi/n)
    pIn = n*sin(pi/n)
    listSides.append(n)
    listpIn.append(pIn)
    listpOut.append(pOut)

#Increase the number of sides (n) to compute pOut - pIn again
    n = n + 1

#print the headers on the list
print '%8s\t%16s\t%16s\t' % ('# Sides','Lower Bound','Upper Bound')
numValues = len(listSides)

#print every 10th element on the list by using mod 10 and formatting for 
#column width, precision, and tabs.
for m in range(numValues):
    if m%(numValues/10) == 0:
        print'%8d\t%16.5f\t%16.5f\t' % (listSides[m],listpIn[m],listpOut[m])        


