# Title: Error in Euler-Cromer Method for Radioactive Decay
# Author: Lisa Carpenter

'''Abstract: An analytical solution for radioactive decay is well known
and can be used to determine the number of atoms left in a radioactive mass
after a period of time. This script uses the Euler-Cromer method for 
numerically calculating the error in radioactive decay number of atoms versus 
the time step.  The Euler-Cromer method differs from the well-known Euler 
method in that it uses the computed values of omega to compute the next 
iteration and uses a half-time step for more accuracy.  As can be seen, 
error increases quadratically as dt increases, but the accuracy of the model
is much higher for low values of t.  Error is proportional to the order of 
the time step multiplied by t/dt.  Since we are keeping higher order terms, 
the error will be of order (dt)^3*t/dt =~ (dt)^2, which is why a quadratic 
correlation between error and time step is observed.'''

from pylab import *

# decay constant (in s)
tau = 1.0

# the time step
dt = arange(0.01, 1.01, 0.01)
numDt = len(dt)
M = zeros([numDt])

for k in range(0, numDt):
    t = 5.0 * tau
    numSteps = t/(dt[k])
    numSteps = int(numSteps)
    N = zeros([numSteps])

    # initialize with 1000 atoms
    N[0] = 1000
    for n in range(1, numSteps):
        dN1 = -N[n-1] / tau
        N1 = N[n - 1] + 0.5 * dt[k] * (dN1)
        dN2 = -(N1) / tau
        N[n] = N[n - 1] + dt[k] * dN2

    # compare to analytical result
    M[k]=abs(N[n] - N[0] * exp(-(numSteps - 1) * dt[k] / tau))
        
plot(dt,M)
xlabel('dt [seconds]')
ylabel('Error [# of Particles]')
suptitle('Error vs. dt in Runge-Kutta 2nd Order Approach to Radioactive Decay')
legend()
show()
