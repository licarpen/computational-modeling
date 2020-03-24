#Assignment Number: 04
data that was acquired from the Error vs dt in nuclear decay plot.  The 
data appears to be linear in nature, so an equation of form y = mx + b
will be used to fit the data.  This is done using the optimize code 
written in class, specifying the function we wish to fit as y = a_0x + a_1.
The program will fit the parameters and a line will be generated using 
plot().  The value of X^2 (X = chi) can be used to determine how well the
line fits the given data.  If the linear regression is a good fit, 
X^2/DOF should be approximately equal to 1.  X^2 = N - M, where 
N = # of data points, and M = # parameters.  Here, X^2 is found to be
0.12.  Since DOF = 2, 0.12/2 = .06, which is low for X^2.  This indicates
that the fit is "too good," perhaps due to the fact that a linear fit was 
used for data that is already known to increase linearly.    
tau = 1.0

# the time step
dt = arange(0.01,1.01,0.01)
#determine the number of iterations
numDt = len(dt)
#create an empty array in which to store the number of atoms for various dt
M = zeros([numDt])

#Create a for loop to iterate through each time step, dt
for k in range(0,numDt):
#initialize the total time to run the Euler-method
    t = 5.0*tau
#Determine the number of steps in this range, dependent of present value of dt
    numSteps = int(t/(dt[k]))
#Create an array to input number of atoms after each iteration
    N = zeros([numSteps])

#Initialize with 1000 atoms
    N[0] = 1000
#Iterate through each time step
    for n in range(1,numSteps):
#Determine number of atoms remaining after time t
        N[n] = (1.0-dt[k]/tau)*N[n-1]
#Calculate error in numerical value for given dt and analytical solution
    M[k]=abs(N[n] - N[0]*exp(-(numSteps-1)*dt[k]/tau))

