# The Dissipative Pendulum
# Author: Lisa Carpenter

'''Abstract: The behavior of a damped pendulum will be investigated.  A
pendulum subject to a frictional damping force has the potential to undergo
three types of motion, being underdamped, critically damped, and overdamped.
The type of motion is dependent on initial conditions and the damping factor,
q.  The value of q will be determined for a set of initial conditions.  This
is done by using the Euler-Cromer method to describe the theta of the pendulum
as a function of time.  In order to determine q, this method is carried out
through a for loop starting with small values of q. Because the motion will
begin underdamped, the oscillations will dop below zero.  Once the motion
oscillates below zero, no further iterations will be performed, and a larger
value of q will be used for the next set of iterations.  Once the entire
range of time values is completed, critically damped motion will be present,
and theta[n] will have a value in its last index.  When this condition is met,
q will be printed and the theta calculations will be terminated by breaking
from loop.  
'''
from pylab import *

#Initialize constants - gravity, length of pendulum
g = 9.81
l = 1.0
#Set end time (seconds)
t = 5.0
#Set time step
dt = 0.001
#Determine number of steps to iterate theta and omega through
numSteps = int(t/dt)
#Create an array of possible q values, beginning at 0.1 and ending at 10
q = arange(0.1,10,0.01)
#Create for loop to iterate through possible values of q
for k in range (len(q)):
#Create array to input values of theta, initialize theta_0 at 0;2 radians
    theta = zeros([numSteps])
    theta[0] = 0.2
#Create array to input values of omega (dtheta/dt) and initialize to 0 r/s
    omega = zeros([numSteps])
    omega[0] = 0.0
#Create for loop to determine theta and omega values using initial
#conditions and incrementing time step by dt
    for n in range(1,numSteps):
#Only continue to input theta values for subsequent t if theta has not
#attained a value below zero.  
        if theta[n-1] > 0:
            omega[n] = omega[n-1] + (-g/l*theta[n-1] - q[k]*omega[n-1])*dt
            theta[n] = theta[n-1] + omega[n]*dt
#Check if a value of theta was stored in final index, indicating that
#theta never dropped below 0 and is critically damped
    if theta[-1] != 0:
        print q[k]
#Break out of loop so further values of q and theta are not calculated
        break

'''Critical damping will occur when q = 2w_0, where w_0 is the natural frequency
of the undadmped pendulum.  For our pendulum, w_0 = sqrt(g/l) = sqrt(9.81/1)
w_0 = 3.13, hence q = 6.26 in the analytical approach.  The error in our
calculation is then abs(6.26 - 6.15)/6.26 = 0.17 = 1.7%.  

'''


            

