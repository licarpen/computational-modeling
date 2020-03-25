# Probability Distribution Functions
# Name: Lisa Carpenter

'''Abstract:This program uses inversion to generate random numbers that look
like the function 1/(a+by)^n, where a = b = 1, n = 3.  The function that
generates the random numbers was found using analytical inversion technique.
The program plots the points generated with a histogram and compares this
result with the actual function that the random numbers are attempting to
mirror.  

'''

from pylab import *
from random import *

#Define number of random numbers to be generated and create array for numbers
numVal = 10**4
y = zeros([numVal])

#Loop through numVal numbers and generate random numbers to input into
#the prob function
for i in range(numVal):
    x = random()
    y[i] = (1/sqrt(1 - x) - 1)
    
#define actual function to compare
def p(x):
    return 2/(1 + x)**3

#Plot random numbers generated in a histogram and plot actual prob function
#Label graph
xp = arange(0,8,0.01)
plot(xp,p(xp))
hist(y, bins = 100, range = (0,10), normed = True)
xlim(0,8)
title('Prob. Dist. Histogram for p(x) = 1/(1+x)^3')
xlabel('[x]')
ylabel('p(x)')
legend()
show()
