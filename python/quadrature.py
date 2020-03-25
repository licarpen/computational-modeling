# Title: Integral Approximation Techniques
# Author: Lisa Carpenter

'''Abstract: This script calculates the integral from -1 to 1 of the fucntion 
f(x) = x^2/cosh(x) in three different ways.  Frist, a bruteforce Monte Carlo 
technique is used, generating random numbers (x_i) in the interval from -1 to 1 
and summing N rectangles of height f(x_i) and width 2/N to approximate the integral.  
The second method approximates each interval as a trapezoid and uses the boundaries 
of the function as h_1 and h_2 of the trapezoid. Finally, importance sampling is used 
to flatten the function, eliminating random values of x_i via the rejection method 
for the function p(x) = 1/cosh(x). The remaining x_i values are used with bruteforce 
to approximate the integral. The integral estimations are calculated for several 
values of N and presented in a table. The error in the importance and bruteforce MC 
method increases as 1/sqrt(N), where N is the number of samples used to calculate the 
integral. This can be shown by graphing error versus 1/sqrt(N).  The resulting 
correlation appears linear. While the trapezoid method of integration results in a 
precise result with N = 100, the MC techniques scale better in higher dimensions and 
require less computation for increased accuracy.'''

from pylab import *
import random as r

def bruteforce(N):
    Sum = 0.0
    for i in range(N):
        x = r.uniform(-1.0,1.0)
        Sum += x**2/cosh(x)
    Int = 2*Sum/N
    return Int

def trapezoid(N):

    def f(x):
        return x**2.0/cosh(x)
    # set bounds
    a = -1.0
    b = 1.0
    Sum = 0.0
    for i in range(1, N):
        Sum = Sum + f(a + (b - a) * i / N)
    # account for behavior at bounds and calculate total integral approximation
    Int = (b - a) / N * (Sum + f(a) / 2.0 + f(b) / 2.0)
    return Int

def importance(N):
    # normalization constant
    c = 1.0/1.73154
    # sampling function from which to generate random x_i values
    def p(x):
        return c / cosh(x)

    def f(x):
        return x**2.0 / cosh(x)

    Nunder = 0
    Sum = 0.0

    # carry out rejection method using sampling function p(x) to acquire x_i values    
    while Nunder < N:
        x1 = r.uniform(-1.0,1.0)
        x2 = r.uniform(0.0,1.0)
        if x2 <= p(x1):
            # accept coordinate pair is accepted
            Sum = Sum + f(x1) / p(x1)
            Nunder += 1
    Int = 1.0 / N * Sum
    return Int

def errBrute(N):
    Int = 0.512022
    return abs(bruteforce(10**N) - Int)

def errImportance(N):
    Int = 0.512022
    return abs(importance(10**N) - Int)

print '%8s\t%8s\t%16s\t%16s\t' % ('N','Bruteforce','Trapezoid','Importance')
for N in range(2,8):
    print'%8.0e%16.5f\t%16.5f\t%16.5f\t' % (10**N,bruteforce(10**N),trapezoid(10**N),importance(10**N))
    scatter(errBrute(N), 1.0/sqrt(10**N), c = 'b')
    scatter(errImportance(N), 1.0/sqrt(10**N), c = 'r')
title('MC Method Error vs. 1/sqrt(N) in Computing Int(-1,1)(x^2/cosh(x)')
xlabel('Error in MC Method')
ylabel('1/sqrt(N)')
show()


