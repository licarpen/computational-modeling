# White Noise
# Author: Lisa Carpenter


'''Abstract:  This script generates a white noise power spectrum
using the Box-Muller method.  An array of 2^10 random numbers is generated and
treated like a time series.  FFT is used to compute the power spectrum of
these values.  The Box-Muller method uses a Gaussian distribution with mean
mu = 0 and sigma^2 = 1.  This probability distribution is then inverted
to find the function from which to draw random numbers, which takes two
values.'''

from pylab import *
import random as r

numVal = 2**10
y = zeros([numVal])

# run Box-Muller function on random coordinate pairs
for i in range(numVal):
    x1 = r.random()
    x2 = r.random()
    y[i] = sqrt(-2 * log(1 - x1)) * cos(2 * pi * x2)

# apply Fast Fourier Transform.
Y = fft(y)

plot(abs(Y))
title('Power Spectrum for Generated White Noise')
xlabel('Time (seconds)')
ylabel('Power (watts)')
xlim(0,1000)
show()
