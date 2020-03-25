# Approximation of e
# Lisa Carpenter

'''Abstract:  This program will estimate the value of "e" using a Monte Carlo
technique.  The definition of e is the upper bound on the integral of 1/x
such that int from 1 to e == 1.  Using change of base formulas, it can be
proven that e = 10^1/A, where A is the value of the integral 1/x from 1 to 10.
This integral is calculated by generated random, uniform numbers between 1 and
10 and using brute force integration to find the sum, and hence the integral.
Then e is calculated using the method described above.  

'''

from pylab import *
import random as r

#Set the bounds of the integral and the number of random numbers
a = 1.0
b = 10.0
N = 10**8

#Initialize the sum
sum = 0.0

#Loop through N random numbers x_i and add to the sum f(x_i) where f(x) = 1/x
for i in range(N):
    x = r.uniform(1.0,10.0)
    sum = (sum + 1/x)
#Calculate total integral of 1/x from 1 to 10. 
A = (b-a)*sum/N
#Calculate the value of e
evalue = 10.0**(1/A)

#Print evalue
print evalue

