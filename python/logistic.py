#Assignment Number: 04
#Question Number: 01: The Logistic Map
#Author: Lisa Carpenter
#Date: 10.09.2011
#File Name: logistic.py

'''Abstract:This program will display a bifurcation diagram mapping the 
logistic equation against the parameter mu.  This will be done using a for loop to 
iterate through values of mu.  For each mu, two additional for loops will 
be used - the first to get rid of transient behavior of the logistic equation
and the second to store values of x_n for several hundred input values.  
The logistic equation will then be mapped against mu using the plotting feature.
Chaos onset and period doubling will be noted using text.  

'''
from pylab import *

#Create array of mu values through which to iterate
mu = arange(1.0,4,0.01)
#Find length
numMu = len(mu)
#Set number of iterations for logistic equation to get rid of transients
numIt1 = 50
#Set number of iterations for logistic equation to map
numIt2 = 200
#Create arrays for storing transients and iterations 
x1 = zeros([numMu,numIt1], dtype = float)
x2 = zeros([numMu,numIt2], dtype = float)
#Iterate through mu values
for n in range(numMu):
    x1[n,0] = 0.5
#For each mu value, get rid of transients by calculating numIt1 values for
#the logistic equation
    for i in range(1,numIt1):
        x1[n,i] = mu[n]*x1[n,i-1]*(1-x1[n,i-1])   
#For each mu value, create list of x_ns for numIt2.  
    for i in range(1,numIt2):
#Set the initial value in the array to the final value from numIt1.
        x2[n,0] = x1[n,-1]
        x2[n,i] = mu[n]*x2[n,i-1]*(1-x2[n,i-1])
#Plot the x_n values versus mu
for j in range(numMu):
    for k in range(numIt2):
        scatter(mu[j],x2[j,k],s = 2)
#Title
title('Bifurcation Diagram for the Logistic Equation')
#Make legend for chaos onset and period doubling
text(0.6,0.9,'Period Doubling = PD')
text(0.6,0.85,'Chaos Onset = CO')
xlabel('Parameter Mu')
ylabel('x_n')
#Place text indicating period doubling and chaos onset. 
text(3.55,0,'CO')
text(3.0,0,'PD')
text(3.4,0,'PD')
show()
