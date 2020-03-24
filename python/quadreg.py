#Assignment Number: 04
#Question Number: 02: Curve Fitting
#Author: Lisa Carpenter
#Date: 10.09.2011
#File Name: quadreg.py

'''Abstract:
Abstract: quadreg.py is a program that will determine a quadratic fit to the 
data that was acquired from the 2nd order Runge Kutta Error vs dt in nuclear decay plot.
The data appears to be quadratic in nature, so an equation of form y = ax^2 + bx + c
will be used to fit the data.  This is done using the optimize code 
written in class, specifying the function we wish to fit as y = a_0x^2 + a_1x + a_2.
The program will fit the parameters and a curve will be generated using 
plot().  
'''

from pylab import *
from scipy import *
from scipy import optimize

#The following is the code used to plot the RK Error vs dt
#in nuclear decay written for the previous assignment:

# decay constant (in s)
tau = 1.0
# the time step
dt = arange(0.01,1.01,0.01)
numDt = len(dt)
M = zeros([numDt])

for k in range(0,numDt):
    t = 5.0*tau
#   ct = arange(0.0,t,dt[k])
    numSteps = t/(dt[k])
    numSteps = int(numSteps)
    N = zeros([numSteps])
#We assume that we start with 1000 atoms
    N[0] = 1000
    for n in range(1,numSteps):
        dN1 = -N[n-1]/tau
        N1 = N[n-1] + 0.5*dt[k]*(dN1)
        dN2 = -(N1)/tau
        N[n] = N[n-1] + dt[k]*dN2
    M[k]=abs(N[n] - N[0]*exp(-(numSteps-1)*dt[k]/tau))

# target function (Y)
fitfunc = lambda p, x: p[0]*x**2 + p[1]*x + p[2]

# error function (Delta)
errfunc = lambda p, x, y: fitfunc(p, x) - y 

# Fit the first set

# Initial guess for the parameters
p0 = [0.0, 0.0, 0.0]

# scipy general leastsquares fitting routine
fit = optimize.leastsq(errfunc, p0, args=(dt, M),full_output=1)

# fit parameters
p1 = fit[0]
    
# covariance matrix
cov1 = fit[1]
# the time array for fitting purposes
time = arange(dt.min(), dt.max(), (dt.max()-dt.min())/100.0)
# Plot the results of the fit
plot(dt, M, linestyle = 'none', marker = 'o')
plot(time, fitfunc(p1, time), "r-")
# Legend the plot
title("Quad Reg Fit for RK-2nd-Order Approach to Error vs. dt for Radioactive Decay")
xlabel("dt [seconds]")
ylabel("Error [# of particles]")
legend(('dt', 'dt-fit', 'Error', 'Error-fit'))
ax = axes()
text(0.1,45, 'Error(dt) = Ax^2 + Bx + C')
text(0.1,40, 'Where A, B, C and covariance = ')
text(0.1,36, p1[0])
text(0.1,33, p1[1])
text(0.1,30, p1[2])
text(0.1,27,cov1[0])
show()
