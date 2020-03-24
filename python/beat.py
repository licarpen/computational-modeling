#Final Project
#Name: Lisa Carpenter
#Date: 12.01.2011
#Filename: beat.py

from pylab import *

#Set initial freqeuncies and time array
f1 = 440.0
f2 = 500.0
t = arange(0.0,0.05,0.0001)

#Loop through several frequencies and generate beat frequency
for i in range(20):
    plot(t,sin(2.0*pi*f1*t),label = 'f1 = 440.0 Hz')
    plot(t,sin(2.0*pi*f2*t),label = 'f2 = '+ str(f2) + ' Hz')
    plot(t,sin(2.0*pi*f2*t)-sin(2.0*pi*f1*t), label = 'f1 + f2')
#Plot data
    title('Superposition of Waves with Similar Frequencies')
    xlabel('X')
    ylabel('Y')
    legend()
    show()

#Change second frequency by 5 Hz to approach f1
    f2 -= 5.0

