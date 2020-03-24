# Title: Error in Euler Method for Radioactive Decay
# Author: Lisa Carpenter

'''Abstract: An analytical solution for radioactive decay is well known
and can be used to determine the number of atoms left in a radioactive mass
after a period of time. This script models the error in the Euler method 
as a function of the time step (dt) used in the Euler approach. Error is
plotted by comparing the difference between the numerical values and each 
analytical value to the time step used.'''

from pylab import *

# decay constant (in s)
tau = 1.0

# time steps
dt = arange(0.01, 1.01, 0.01)
numDt = len(dt)

# will store the number of atoms for various dt
M = zeros([numDt])

for k in range(0, numDt):
    # total time to run the Euler-method
    t = 5.0 * tau
    numSteps = int(t / (dt[k]))
    N = zeros([numSteps])

    # initialize with 1000 atoms
    N[0] = 1000
    for n in range(1, numSteps):
        # Euler method prediction of atoms remaining after time t
        N[n] = (1.0 - dt[k] / tau) * N[n - 1]
    # error in numerical value for given dt given analytical solution
    M[k] = abs(N[n] - N[0] * exp(-(numSteps - 1) * dt[k] / tau))

# plot the error as a function of dt
plot(dt,M)
xlabel('dt [seconds]')
ylabel('Error [# of Particles]')
suptitle('Error vs. dt in Euler Method for Radioactive Decay')
legend()
show()

'''In analyzing the plot of error versus dt, it appears that error as a
function of dt is linear.  The error per step is actually dt^2.
However, throughout the entire Euler calculation, t/dt time steps are used,
and thus the error is proportional to the product of these two values -
(dt^2) * t/dt =~ dt.  Thus, as time step increases, the error increases
linearly as well.'''
