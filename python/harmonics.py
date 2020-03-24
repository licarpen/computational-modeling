#Final Project
#Name: Lisa Carpenter
#Date: 12.01.2011
#Filename: harmonics.py

from pylab import *

#Get x values
x = arange(0,pi/2,0.01)
#Create color list for plot
c = array(['r','b','g','m','k'])

#Loop through 4 frequencies and plot both positive and negative
for n in range(1,5):
    plot(x,sin((2*n-1)*x), color = c[n-1], linewidth = 3, label = 'Harmonic ' + str(n))
    plot(x, -sin((2*n-1)*x), color = c[n-1], linewidth = 3)
#Label plot
title('Harmonics for A Hollow Pipe Closed at One End')
xlabel('X [Length of Pipe]')
ylabel('Y [Pipe Diamter]')
legend()
show()
