#Final Project
#Name: Lisa Carpenter
#Date: 12.01.2011
#Filename: guitar.py

'''Abstract: This program simulates the displacement of a string after it
is plucked.  See Poject Paper for further details.  

'''

from pylab import *

#Initialize length of string, time array, r-value, and y-array for displacement
M = 52
t = arange(0,501,1)
T = len(t)
y = zeros([M,T])
r = 0.75

#Set the initial displacement of the string when plucked from center
for i in range(1,35):
    y[i,0] = y[i-1,0]+0.1
for i in range(36,M-1):
    y[i,0] = y[i-1,0] - 0.2

#Calculate displacement along the string for each time t.
for n in range(1,T-1):
    for i in range(1,M-1):
        y[i,n+1] = 2*(1-r**2)*y[i,n] - y[i,n-1] + r**2*(y[i+1,n] + y[i-1,n])

#Perform a Fast Fourier Transform at x = 45 to determine resultant frequencies
Y = fft(y[45,:])

#Plot the displacement of the string at each time segment
figure(1)
plot(y[:,:])
title('Displacement of Guitar String Plucked Off-Center')
xlabel('X')
ylabel('Y')

#Plot behavior of center of string as a function of time
figure(2)
plot(t,y[M/2-1,:])

#Plot power spectrum
figure(3)
plot(abs(Y))
xlim(0,40)

show()
