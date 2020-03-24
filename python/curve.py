#Assignment Number: 04#Question Number: 02: Curve Fitting#Author: Lisa Carpenter#Date: 10.09.2011#File Name: linreg.py'''Abstract:'''from pylab import *from scipy import *from scipy import optimize#The following is the code used to plot the Error vs dt#in nuclear decay written for the previous assignment:# decay constant (in s)
tau = 1.0

# the time step
dt = arange(0.01,1.01,0.01)
#determine the number of iterations
numDt = len(dt)
#create an empty array in which to store the number of atoms for various dt
M = zeros([numDt])

#Create a for loop to iterate through each time step, dt
for k in range(0,numDt):
#initialize the total time to run the Euler-method
    t = 5.0*tau
#Determine the number of steps in this range, dependent of present value of dt
    numSteps = int(t/(dt[k]))
#Create an array to input number of atoms after each iteration
    N = zeros([numSteps])

#Initialize with 1000 atoms
    N[0] = 1000
#Iterate through each time step
    for n in range(1,numSteps):
#Determine number of atoms remaining after time t
        N[n] = (1.0-dt[k]/tau)*N[n-1]
#Calculate error in numerical value for given dt and analytical solution
    M[k]=abs(N[n] - N[0]*exp(-(numSteps-1)*dt[k]/tau))# target function (Y)fitfunc = lambda p, x: p[0]*x + p[1]    # error function (Delta)errfunc = lambda p, x, y: fitfunc(p, x) - y     # Fit the first set    # Initial guess for the parametersp0 = [0.0, 0.0]    # scipy general leastsquares fitting routinefit = optimize.leastsq(errfunc, p0, args=(dt, M),full_output=1)    # fit parametersp1 = fit[0]        # covariance matrixcov1 = fit[1]#yerr = zeros([numSteps],dtype = float)#for i in range numsteps:#    yerr[i] = errfunc(dt)    # the time array for fitting purposestime = arange(dt.min(), dt.max(), (dt.max()-dt.min())/100.0)#errorbar(dt, M, yerr=errfunc,linestyle='None',marker='s',markersize=10,capsize=6)    # Plot the results of the fitplot(dt, M, linestyle = 'none', marker = 'o')plot(time, fitfunc(p1, time), "r-")    # Legend the plottitle("Quad Reg Fit for RK-2nd-Order Approach to Error vs. dt for Radioactive Decay")xlabel("dt [seconds]")ylabel("Error [# of particles]")legend(('dt', 'dt-fit', 'Error', 'Error-fit'))ax = axes()text(0.1,30, 'Error(dt) = mx + b')text(0.1,25, 'Where m, b, and covariance = ')text(0.1,21, p1[0])text(0.1,18, p1[1])text(0.1,15,cov1[0])show()


