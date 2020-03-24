#File Name: knuckleball.py
#Assignment: 03
#Problem: 2: The Knuckleball
#Author: Lisa Carpenter
#Date: 09.21.2011

'''Abstract:The knuckleball.py program will display a colorful spectral-map
indicative of knuckleball pitch spatial coordinates at the batter.  This will be
accomplished by using Newtonian Mechanics to describe the trajectory and using
Euler method to iterate through time steps to determine the the placement in
the z and y directions.  The final data will be stored in a 10 x 10 array,
depicting the batter's spatial array, i.e. strike zone.  This will be
accomplished by taking the spatial coordinate and translating it into an integer
between 1 and 10, representing a row or column index in the array. A histogram
will show the probability that a knuckleball will strike a particular box the size
of a baseball.  
'''
from pylab import *
import random

#Define function for the lateral force on the knuckleball
def Fknuck(theta):
    g = 9.8 # N/kg acceleration due to gravity
    Fom = 0.5*g*(sin(4.0*theta) - 0.25*sin(8.0*theta) + \
                0.08*sin(12.0*theta) - 0.025*sin(16.0*theta))
    return Fom

# --------------------------------------------------------------------
#Define function for the drag force on the baseball
def Fdrag(v):
    vd = 35.0 # m/s
    Delta = 5.0 # m/s
    return 0.0039 + 0.0058/(1.0 + exp((v-vd)/Delta))

# --------------------------------------------------------------------

# main program
def main():

# constants of nature
    g = 9.8 # N/kg
# the time step
    dt = 0.01 # s
# initialize arrays to put z and y position into after placement calculation
    zPos = zeros([20000])
    yPos = zeros([20000])
#Iterate through 20000 random variables
    for n in range(20000):
#Initialize all variables and randomize variables
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
#Iterate spatial position while the ball travels to the batter, but not beyond
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
#Shift z and y position into the array that represents the batter's strike zone
        zPos[n] = z[-1] + 0.457
        yPos[n] = y[-1] 
#Create array to represent the strike zone
    baseballArray = zeros([10,10])
#Determine the length of one side of a box in the spatial array
    dz = 0.914/10
    dy = 0.914/10
#Initialize variables to input y and z indeces
    zbox = 0
    ybox = 0
#Determine for each knuckball trajectory the spatial placement in y and z.  
    for k in range(20000):
#Take only positions that lie within the strike zone.  
        if zPos[k] >= 0:
            if zPos[k] <= 0.914:
                zbox = int(zPos[k]/dz)
                if yPos[k] >= 0:
                    if yPos[k] <= 0.914:
#If the trajectory makes it to the strike zone, add it to the correct array box
                        ybox = int(yPos[k]/dy)
                        baseballArray[ybox,zbox] += 1
#Normalize the array by dividing by the number of trials
    baseballArray = baseballArray/20000
#Plot a figure showing the spectral density of the strike zone.  
    figure(1)
    imshow(baseballArray, cmap = cm.spectral, origin = 'lower', interpolation = 'nearest', extent=[-1.5,1.5,0,3])
    colorbar()
    xlabel('Z-Axis (meters)')
    ylabel('Y-Axis (meters)')
    suptitle('Figure 1: Density of Knuckleball Placement')
    show()


        
if __name__ == '__main__':
    main()




