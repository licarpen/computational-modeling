# Title: Density of Knuckleball Placement
# Author: Lisa Carpenter

'''Abstract: A knuckleball is a pitch thrown in baseball that minimizes spin on
the ball, resulting in an erratic trajectory.  This script models a knuckleball 
with a spectral map showing probabilistic spatial coordinates when the ball reaches
the batter, i.e. the strike zone.  This is accomplished by using Newtonian Mechanics 
to describe the trajectory and using the Euler method to iterate through time steps 
to determine the placement in the z and y directions. A histogram (not shown) displays
the probability that a knuckleball will strike a particular box the size of a baseball.
'''

from pylab import *
import random

# lateral force on the knuckleball
def Fknuck(theta):
    g = 9.8 # N/kg acceleration due to gravity
    Fom = 0.5 * g * (sin(4.0 * theta) - 0.25 * sin(8.0 * theta) + \
                0.08 * sin(12.0 * theta) - 0.025 * sin(16.0 * theta))
    return Fom

# drag force on the baseball
def Fdrag(v):
    vd = 35.0 # m/s
    Delta = 5.0 # m/s
    return 0.0039 + 0.0058 / (1.0 + exp((v - vd) / Delta))

# main program
def main():
    g = 9.8 # N/kg
    dt = 0.01 # s
    zPos = zeros([2000])
    yPos = zeros([2000])
    # compute 20000 knuckleball trajeectories
    for n in range(2000):
        x = array([0.0])
        y = array([random.uniform(2.19,2.31)])
        z = array([0.0])
        cx = x[0]
        cy = y[0]
        cz = z[0]
        vx = random.uniform(28.2,30.0)
        vy = random.uniform(-0.0894,0.0894)
        vz = 0.0
        omega = random.uniform(0.15*2*pi,0.25*2*pi)
        theta = 2.0*pi*random.random()
        # iterate spatial position while the ball travels to the batter
        while x[-1] < 18:
            theta += omega * dt
            v = sqrt(vx**2 + vy**2 + vz**2)
            vx -= Fdrag(v) * v * vx * dt
            vy -= g*dt + Fdrag(v) * v * vy * dt
            vz += -Fdrag(v) * v * vz * dt + Fknuck(theta)*dt
            cx += vx * dt
            cy += vy * dt
            cz += vz * dt
            x = append(x,cx)
            y = append(y,cy)
            z = append(z,cz)
        # shift z and y position into the array that represents the batter's strike zone
        zPos[n] = z[-1] + 0.457
        yPos[n] = y[-1] - 0.914
    baseballArray = zeros([10,10])
    dz = 0.914/10
    dy = 0.914/10
    zbox = 0
    ybox = 0
    # determine the spatial placement in y and z for each knuckball trajectory
    for k in range(2000):
        # add positions that lie within the strike zone to array box
        if zPos[k] >= 0:
            if zPos[k] <= 0.914:
                zbox = int(zPos[k]/dz)
                if yPos[k] <= 0:
                    if yPos[k] >= -0.914:
                        ybox = int(-1*yPos[k]/dy)
                        baseballArray[zbox,ybox] += 1
    # normalize
    baseballArray = baseballArray/2000

    figure(1)
    hist(baseballArray)
    suptitle('Figure 1: Histogram of Knuckleball Placement')
    xlabel('Bin Number')
    ylabel('Probability') 
    figure(2)
    imshow(baseballArray, cmap = cm.spectral, origin = 'lower')
    colorbar()
    xlabel('Z-Axis (meters)')
    ylabel('Y-Axis (meters)')
    suptitle('Figure 2: Density of Knuckleball Placement')
    show()
        
if __name__ == '__main__':
    main()




