#Final Project
#Name: Lisa Carpenter
#Date: 12.01.2011
#Filename: drum.py

from pylab import *
from scipy.special import jn
from scipy.special import jn_zeros

#Create time array, position array, and lamda array
t = arange(0.0,3.0,0.01)
T = len(t)
lam = zeros([10])
a = 0.5
u = zeros([T])


figure(1)
#Initialize r-location for observing motion
r = 0.0
#Cycle through first 4 modes by changing lambda
for j in range (4):
    for i in range(T):
        lam[j] = jn_zeros(0,10)[j]
#Get height at every time segment
        u[i] = (cos(lam[j]*t[i])+sin(lam[j]*t[i]))*jn(0,lam[j]/a*r)            
#Plot all data and label
    plot(t,u, label = 'n-th zero, n = ' + str(j+1),linewidth = 2)
title('Y Displacement of a Circular Drumhead at r = 0.0')
xlabel('Time [seconds]')
ylabel('Y Displacement')
legend()
show()

figure(2)
#Initialize r-location for observing motion
r = 0.3
#cycle through first 4 modes by changing lambda
for j in range (4):
    for i in range(T):
        lam[j] = jn_zeros(0,10)[j]
#Get height at everl time segment
        u[i] = (cos(lam[j]*t[i])+sin(lam[j]*t[i]))*jn(0,lam[j]/a*r)            
#plot all data and label
    plot(t,u, label = 'n-th zero, n = ' + str(j+1), linewidth = 2)
title('Y Displacement of a Circular Drumhead at r = 0.3')
xlabel('Time [seconds]')
ylabel('Y Displacement')
legend()
show()
