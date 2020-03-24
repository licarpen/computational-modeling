# Title: Logistic Bifurcation Diagram
# Author: Lisa Carpenter
# File Name: logistic.py

'''Abstract:This program displays a bifurcation diagram mapping the 
logistic equation against the parameter mu. The logistic equation is defined iteravely as x_n+1 = mu * x_n (1 - x_n). For each value of mu, transient behavior of the logistic equation is eliminated and values of x_n are recorded. Chaos onset and period doubling are denoted on the diagram.'''

import pylab as pl

def main():

    mu = pl.arange(1.0,4,0.01)
    numMu = len(mu)
    numIt1 = 50
    numIt2 = 200

    x1 = pl.zeros([numMu, numIt1], dtype = float)
    x2 = pl.zeros([numMu, numIt2], dtype = float)

    for n in range(numMu):
        x1[n, 0] = 0.5
        # eliminate transients
        for i in range(1, numIt1):
            x1[n, i] = mu[n] * x1[n, i - 1] * (1 - x1[n, i - 1])    
        for i in range(1, numIt2):
            # Set initial value to final value from numIt1.
            x2[n, 0] = x1[n, -1]
            x2[n, i] = mu[n]*x2[n, i - 1]*(1 - x2[n, i - 1])

    # plot the x_n values versus mu
    for j in range(numMu):
        for k in range(numIt2):
            pl.scatter(mu[j], x2[j,k], s = 2)

    pl.title('Bifurcation Diagram for the Logistic Equation')
    pl.text(0.6, 0.9, 'Period Doubling = PD')
    pl.text(0.6, 0.85, 'Chaos Onset = CO')
    pl.xlabel('Parameter Mu')
    pl.ylabel('x_n')
    pl.text(3.55, 0, 'CO')
    pl.text(3.0, 0, 'PD')
    pl.text(3.4, 0, 'PD')
    pl.show()

if __name__ == '__main__':
    main()