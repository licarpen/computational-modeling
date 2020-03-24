# random_walk_prob.py
# Adrian Del Maestro
# 11/06/2011

# Study a one dimenisional random walk, with equal probability for left and
# right jumps with size 1.

import numpy as np
import pylab as pl

# -----------------------------------------------------------------------------
def step():
    '''Generate a random step, either left or right 1 unit. '''
    if np.random.random() < 0.5: 
        return -1
    else: 
        return 1

# -----------------------------------------------------------------------------
def pbc(x,L):
    ''' Enforce Periodic boundary conditions for a 1D system of length L.'''
    if x < -L/2:
        x += L
    if x >= L/2:
        x -= L
    return x

# -----------------------------------------------------------------------------
def mc_trial(L,numSteps,x,x2,prob):
    ''' Do a Monte Carlo trial, that corresponds to random-walking one
    particle.'''

    cx = 0;
    for s in range(numSteps):
        cx += step()

        # enforce PBC
        cx = pbc(cx,L)

        # Update the position and posistion^2 array
        x[s] += cx
        x2[s] += cx**2

        # Update the probability
        prob[cx + L/2] += 1

# -----------------------------------------------------------------------------
# main program
# -----------------------------------------------------------------------------
def main():

    # The system size
    L = 100

    # number of steps
    numSteps = 1000

    # number of walkers
    numWalkers = 1000
    
    # the main data arrays for holding x and x^2
    x = np.zeros([numSteps],dtype=float)
    x2 = np.zeros([numSteps],dtype=float)

    # The probablity array
    prob = np.zeros([L],dtype=float)

    # Wait to continue
    fig = pl.figure(1)
    test = raw_input('Press Enter to start the random walks.')
    px = range(-L/2,L/2)

    for walker in range(numWalkers): 
        mc_trial(L,numSteps,x,x2,prob)
        if walker % 10 == 0:
            fig.clear()
            pl.bar(px,prob/sum(prob),width=1.0, color='white', edgecolor='teal', linewidth=0.5)
            pl.xlabel('x')
            pl.ylabel(r'$w(x,%d)$' % numSteps)
            pl.xlim(-L/2,L/2)
            pl.draw()

    # normalize
    prob /= 1.0*numWalkers*numSteps

    # figure 1
    # plot the final probability distribution
    fig.clear()
    pl.bar(px,prob,width=1.0, color='white', edgecolor='teal', linewidth=0.5)
    pl.xlabel('x')
    pl.ylabel(r'$w(x,%d)$' % numSteps)
    pl.xlim(-L/2,L/2)
    pl.title('Random Walk in 1D')

    pl.show()

if __name__ == '__main__':
    main()
