#Assignment #: 05
#Question #: 03: Quadrature
#Name: Lisa Carpenter
#Date: 11.08.2011
#Filename: quad.py

'''Abstract:
This program will calculate the integral from -1 to 1 of the fucntion f(x) = x**2/cosh(x)
in three different ways.  Frist, a bruteforce Monte Carlo technique will be used,
generating random numbers (x_i) in the interval from -1 to 1 and adding up N rectangles
of height f(x_i) and width 2/N to approximate the integral.  The second method will be
the trapezoidal rule, approximating each interval as a trapezoid and using the boundaries
of the function as h_1 and h_2 of the trapezoid.  Finally, importance sampling will be
used to flatten the function, using only random value of x_i that are accepted using the
rejection method for the function p(x) = 1/cosh(x). After a set of random x_i's are found
that satisfy this condition, the values will then be used with bruteforce to approximate
the integral.  The integral estimations will be calculated for several values of N and
presented in a table.  The error in the importance and bruteforce MC method goes as 1/sqrt(N),
where N is the number of samples used to calculate the integral.  This can be shown by
mapping the error versus 1/sqrt(N).  The resulting relationship should be linear.  WHile
the trapezoid method of integration results in a precise result with N = 100, the MC
techniques scale better in higher dimensions and require less calculations (lower N) for
more accuracy in the result.  

'''

from pylab import *
import random as r

#Define fucntion to carry out bruteforce integration
def bruteforce(N):
#Initialize sum
    Sum = 0.0
#Loop through each random x_i value within the bounds of the integral
    for i in range(N):
#Generate random x_i values between -1 and 1
        x = r.uniform(-1.0,1.0)
#Add to the total integral sum for each x_i value
        Sum += x**2/cosh(x)
#Compute the final integral by multiplying by (b - a)/N
    Int = 2*Sum/N
    return Int

#Define function to carry out trapezoidal integration
def trapezoid(N):

#Define function to be integrated
    def f(x):
        return x**2.0/cosh(x)
#Set bounds
    a = -1.0
    b = 1.0
#Initialize sum
    Sum = 0.0
#Loop through all x_i values, calculating the next x_i by adding larger even intervals
    for i in range(1,N):
        Sum = Sum + f(a+(b-a)*i/N)
#Account for behavior at bounds and calculate total integral estimation
    Int = (b-a)/N*(Sum + f(a)/2.0 + f(b)/2.0)
    return Int

#Define function to carry out importance sampling                        
def importance(N):
#Define normalization constant
    c = 1.0/1.73154
#Define sampling function from which to generate random x_i values
    def p(x):
        return c/cosh(x)

#Define function to be integrated
    def f(x):
        return x**2.0/cosh(x)

#Set number of accepted values to 0 for rejection method
    Nunder = 0
#Initialize sum
    Sum = 0.0

#Carry out rejection method using sampling function p(x) to acquire x_i values    
    while Nunder < N:
        x1 = r.uniform(-1.0,1.0)
        x2 = r.uniform(0.0,1.0)
#Check to see if coordinate pair lies under the p(x) function
        if x2 <= p(x1):
#If coordinate pair is accepted, use it to add to the integral approximation
            Sum = Sum + f(x1)/p(x1)
#Add to rejection/acceptance counter
            Nunder += 1
#Calculate total value of estimated integral
    Int = 1.0/N*Sum
    return Int
#Calculate the error in various methods
def errBrute(N):
    Int = 0.512022
    return abs(bruteforce(10**N) - Int)
def errImportance(N):
    Int = 0.512022
    return abs(importance(10**N) - Int)

#Display data, cycling through several values of N
print '%8s\t%8s\t%16s\t%16s\t' % ('N','Bruteforce','Trapezoid','Importance')
for N in range(2,8):
#Print and label data in columns
    print'%8.0e%16.5f\t%16.5f\t%16.5f\t' % (10**N,bruteforce(10**N),trapezoid(10**N),importance(10**N))
#Show error versus 1/qrt(N)
    scatter(errBrute(N), 1.0/sqrt(10**N), c = 'b')
    scatter(errImportance(N), 1.0/sqrt(10**N), c = 'r')
#Label graph
title('MC Method Error vs. 1/sqrt(N) in Computing Int(-1,1)(x^2/cosh(x)')
xlabel('Error in MC Method')
ylabel('1/sqrt(N)')
show()


