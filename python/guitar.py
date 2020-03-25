#Final Project
#Name: Lisa Carpenter
#Date: 12.01.2011
#Filename: guitar.py

'''Abstract: This script models the displacement of a string after it
is plucked at 1/2 and 2/3 of the string length. Known equations for y 
displacement and velocity of a wave traveling on a string are used given 
parameters of string tension, density, initial displacement, and length. 
Frequency spectrum at 90% of string length is also generated (not shown). 
Fast Fourier Transforms are used to identify resultant frequencies. 
'''

from pylab import *

#Initialize length of string, time array, r-value, and y-array for displacement
M1 = 51
t = arange(0,501,1)
T = len(t)
y1 = zeros([M1,T])
r = 0.75

#Set the initial displacement of the string when plucked from center
for i in range(1,(M1-1)/2):
    y1[i,0] = y1[i-1,0]+0.1
for i in range((M1-1)/2,M1-1):
    y1[i,0] = y1[i-1,0] - 0.1

#Calculate displacement along the string for each time t.
for n in range(1,T-1):
    for i in range(1,M1-1):
        y1[i,n+1] = 2*(1-r**2)*y1[i,n] - y1[i,n-1] + r**2*(y1[i+1,n] + y1[i-1,n])

#Perform a Fast Fourier Transform at x = 45 to determine resultant frequencies
Y1 = fft(y1[45,:])

#Initialize length of string, time array, r-value, and y-array for displacement
M2 = 52
y2 = zeros([M2,T])

#Set the initial displacement of the string when plucked from center
for i in range(1,35):
    y2[i,0] = y2[i-1,0]+0.1
for i in range(36,M2-1):
    y2[i,0] = y2[i-1,0] - 0.2

#Calculate displacement along the string for each time t.
for n in range(1,T-1):
    for i in range(1,M2-1):
        y2[i,n+1] = 2*(1-r**2)*y2[i,n] - y2[i,n-1] + r**2*(y2[i+1,n] + y2[i-1,n])

#Perform a Fast Fourier Transform at x = 45 to determine resultant frequencies
Y2 = fft(y2[45,:])

#Plot the displacement of the string at each time segment
figure(1)
plot(y1[:,:])
title('Displacement of Guitar String Plucked at Center')
xlabel('X')
ylabel('Y')
xlim(0,50)

#Plot the displacement of the string at each time segment
figure(2)
plot(y2[:,:])
title('Displacement of Guitar String Plucked at 2/3 Length of String')
xlabel('X')
ylabel('Y')
xlim(0,51)

#Plot behavior of center of string as a function of time
figure(3)
plot(t,y1[M1/2-1,:], label = 'Plucked at Center')
plot(t,y2[M2/2-1,:], label = 'Plucked at x = 34')
title('Y Displacement at the Center of the String')
xlabel('Time [seconds]')
ylabel('Y Displacement [meters]')
legend()

#Plot power spectrum
figure(4)
plot(abs(Y1),label = 'Plucked at Center')
plot(abs(Y2), label = 'Plucked at x = 34')
xlim(0,40)
title('Frequency Spectrum at x = 90% of String Length')
xlabel('Frequency [Hz]')
ylabel('Power [Watts]')
legend()


show()
