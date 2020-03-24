# relax-laplace.py
# Adrian Del Maestro
# 10/04/2011

# Employ the Jacobi relaxation method to solve the Laplace Equation in 2D

import pylab as pl
import random


# -----------------------------------------------------------------------------
def init(N,V,Vp):
    '''Initialize the potential with boundary conditions.'''

    # set the boundary conditions for x
    V[:,0] = -1.0
    V[:,N-1] = 1.0

    Vp[:,0] = -1.0
    Vp[:,N-1] = 1.0

    # set the boundary conditions for y
    for j in range(N):
        V[0,j] = -1.0 + 2.0*j/(N-1)
        V[N-1,j] = V[0,j]
        Vp[0,j] = V[0,j]
        Vp[N-1,j] = V[0,j]

    # intialize everything else to zero
    for i in range(1,N-1):
        for j in range(1,N-1):
            V[i,j] = random.random()

# -----------------------------------------------------------------------------
def update(N,V,Vp):
    '''Update the potential according to the Jacobi method.'''

    dV = 0.0
    # intialize everything else to a random values
    for i in range(1,N-1):
        for j in range(1,N-1):
            Vp[i,j] = 0.25*(V[i-1,j] + V[i+1,j] + V[i,j+1] + V[i,j-1])
            dV += abs(Vp[i,j]-V[i,j])

    return dV

# -----------------------------------------------------------------------------
# main program
# -----------------------------------------------------------------------------
def main():
    # the number of lattice points in the x and y direction
    N = 10

    # Create the two arrays needed to store the old and new value of V
    V  = pl.zeros([N,N],dtype=float)
    Vp = pl.zeros([N,N],dtype=float)

    # initialize 
    init(N,V,Vp)

    # Plot the initial conditions
    pl.figure(1,(10,8))
    pl.xlabel('x [m]')
    pl.ylabel('y [m]')
    pl.imshow(V,cmap=pl.cm.jet,extent=[-1,1,-1,1],origin='lower')
    cb = pl.colorbar()
    cb.ax.set_ylabel('Electrical Potential [V]',rotation=-90)
    pl.draw()

    # Wait to continue
    test = raw_input('Press Enter to start the relaxation.')

    # perform a single iteration
    dV = update(N,V,Vp)
    dV += update(N,Vp,V)

    # Now, iterate until convergence
    n = 0
    while dV/(N*N) > 1.0E-5:
        dV = update(N,V,Vp)
        dV += update(N,Vp,V)

        # plot the intermediate results
        if n < 20:
            pl.imshow(V,cmap=pl.cm.jet,extent=[-1,1,-1,1],origin='lower')
            pl.draw()
            print "dV = %8.5E" % (dV/(N*N))
        n += 1

    print "Relaxation Finished."
    print "dV = %8.5E" % (dV/(N*N))

    # plot the final result
    pl.imshow(V,cmap=pl.cm.jet,extent=[-1,1,-1,1],origin='lower')

    pl.show()

if __name__ == '__main__':
    main()
