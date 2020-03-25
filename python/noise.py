#Assignment #: 05
#Question #: 01: White Noise
#Name: Lisa Carpenter
#Date: 11.08.2011
#Filename: noise.py

'''Abstract:  This program will generate a white noise power spectrum
using the Box-Muller method.  An array of 2^10 random numbers is generated and
treated like a time series.  FFT is used to compute the power spectrum of
these values.  The Box-Muller method uses a Gaussian distribution with mean
mu = 0 and sigma^2 = 1.  This probability distribution is then inverted
to find the function from which to draw random numbers, which takes two
values.  

'''

from pylab import *
import random as r

#Set number of values to be generated and create array of zeros to store values
numVal = 2**10
y = zeros([numVal])

#Loop through 2^10 random sets of x1 and x2 coordinates and input into
#Box-Muller function, storing in the array as values are generated
for i in range(numVal):
    x1 = r.random()
    x2 = r.random()
    y[i] = sqrt(-2*log(1 - x1))*cos(2*pi*x2)

#Transform the values in the array using FFT.
Y = fft(y)

#Plot and label the resulting power spectrum.  
plot(abs(Y))
title('Power Spectrum for Generated White Noise')
xlabel('Time (seconds)')
ylabel('Power (watts)')
xlim(0,1000)
show()
