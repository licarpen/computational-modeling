#File Name: rk-radio-active.py
#Assignment: 03
#Question Number: 1: Discretization Error in the Numerical Derivative
#Author: Lisa Carpenter
#Date: 09.20.2011

'''Abstract:  rk-radio-active.py is similar in implementation to radio-active.py
See radio-active.py for methods used.  This program uses the Euler-Cromer
method for numerically calculating the error in radioactive decay number of
atoms versus the time step.  The Euler-Cromer method differs in the fact that
it uses the computed values of omega to compute the next iteration and uses
a half-time step for more accuracy.  As can be seen, error increases
quadratically as dt increases, but the accuracy of the model is much higher
for low values of t.  As noted in radio-active.py, error is proportional to
the order of the time step multiplied by t/dt.  Since we are keeping higher
order terms, the error will be of order (dt)^3*t/dt =~ (dt)^2, which is why
we see a quadratic relationship between error and time step.  
'''
from pylab import *

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
# the number array
  #  print len(ct),numSteps
    N = zeros([numSteps])

#We assume that we start with 1000 atoms
    N[0] = 1000
    for n in range(1,numSteps):
        dN1 = -N[n-1]/tau
        N1 = N[n-1] + 0.5*dt[k]*(dN1)
        dN2 = -(N1)/tau
        N[n] = N[n-1] + dt[k]*dN2

   # plot(ct,N)
    M[k]=abs(N[n] - N[0]*exp(-(numSteps-1)*dt[k]/tau))
        
# Now let us plot the results and compare with the analytic results

#Error as a function of time step dt:



# Plot the error


plot(dt,M)


# now the analytical solution
#anLabel = r'$N(0)\mathrm{e}^{-t/\tau}$'
#plot(t,N[0]*exp(-t/tau),linestyle='-',marker='None',linewidth=1.5,color='black',\
 #          label=anLabel)

# set the plot labels
xlabel('dt [seconds]')
ylabel('Error [# of Particles]')
suptitle('Error vs. dt in Runge-Kutta 2nd Order Approach to Radioactive Decay')
# draw the legend
legend()
# draw the graph to the screen
show()
