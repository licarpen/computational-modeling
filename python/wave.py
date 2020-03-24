#brass.py

from pylab import *


x = arange(0,pi/2,0.01)


for n in range(1,5):
    plot(x,sin((2*n-1)*x))
    plot(x, -sin((2*n-1)*x))
show()

'''
numSteps = len(x)
numHarmonics = 3
data = zeros([numHarmonics,numSteps])
for n in range(numHarmonics):
    for i in range(numSteps):
        data[n,i] = sin(n*i)
        i += 0.01
plot(data)
show()
'''
