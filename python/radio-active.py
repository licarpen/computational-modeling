#File Name: radio-active.py
#Assignment: 03
#Question Number: 1: Discretization Error in the Numerical Derivative
#Author: Lisa Carpenter
#Date: 09.20.2011

'''Abstract: The analytical solution for radioactive decay is well known,
and can be used to determine the number of atoms left after a period of time.
Radio-active.py is a program that will calculate the number of atoms using
an iterative approach, i.e. the Euler method.  This progrom will calculate
the error in the Euler method as a function of the time step (dt) used in the
Euler approach.  This will be done by initializins values and then creating
an array for the number of atoms at each unit of time. The time step will be
changed within a loop, and for each time step, a for loop will be used
to calculate each value of N, storing each value into an array.  The
subsequent N value will be computed by pulling the previous computed value
N-1 from the array.  The error will be plotted by comparing difference between
the numerical values and each analytical value to the time step used.

'''
from pylab import *

# decay constant (in s)
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
    M[k]=abs(N[n] - N[0]*exp(-(numSteps-1)*dt[k]/tau))
# Plot the error as a function of dt
plot(dt,M)
# set the plot labels
xlabel('dt [seconds]')
ylabel('Error [# of Particles]')
suptitle('Error vs. dt in Euler Method for Radioactive Decay')
# draw the legend
legend()
# draw the graph to the screen
show()

'''In analyzing the plot of error versus dt, it appears that error as a
function of dt is linear.  The error per step is actually dt^2.
However, throughout the entire Euler calculation, t/dt time steps are used,
and thus the error is proportional to the product of these two values -
(dt^2) * t/dt =~ dt.  Thus, as time step increases, the error increases
linearly as well.'''
