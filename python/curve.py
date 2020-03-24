#Assignment Number: 04
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

