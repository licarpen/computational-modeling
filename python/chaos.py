#Assignment Number: 03
#Question Number: 04: Chaos and the Lyapunov Exponent
#Author: Lisa Carpenter
#Filename: chaos.py
#Date: 09.27.2011

'''Abstract:A driven and damped pendulum will exhibit chaotic behavior if
initial conditions are set appropriately. The chaotic behavior will be investigated
by looking at the behavior of two pendulums with slightly different initial
conditions.  The value for theta as a function of time for a driven/damped pendulum
will be determined by using the Euler-Cromer method.  When log of the difference in
thetas is plotted against t, chaotic behavior will be evident for small time scales,
and the difference in thetas will increase linearly as time goes on.  This is
indicative of a chaotic system. Because a semi-log y plot show a linear trend,
delta theta = exp[lambda*t), where lambda is the slope of the semi log graph,
and lambda is a parameter called the Lyapunov Exponent.  This parameter is
characteristic of chaotic behavior.  The Lyapunov Exponent for this behavior is
determined visually to be around 0.0039, with a y-intercept of 1E-05.  When
the Lyapunov Exponent transitions between negative and positive values,
the chaotic regime has been met, which is what we see in our case.  

'''

from pylab import *

#Set initial variables: gravity, length of pendulum, damping q, end time,
#dt, and driving force Fd
g = 9.81
l = 9.81
q = 0.5
t_end = 120.0
dt = 0.01
Fd = 1.2
#Determine the number of steps to iterate through
numSteps = int(t_end/dt)
#Set up an array to pull each time step from, beginning at 0, ending at
#t_end, with increment dt
t = arange(0.0,t_end,dt)
#Create arrays for two different values of theta as a function of time
theta1 = zeros([numSteps])
theta2 = zeros([numSteps])
#Initialize theta for both arrays, differing by 0.001 in order to
#investigate chaotic behavior for small change in initial conditions
theta1[0] = 0.2
theta2[0] = 0.201
#Create arrays for the angular frequency, omega, which will be used to
#calculate the subsequent values of theta1 and theta2.
omega1 = zeros([numSteps])
omega2 = zeros([numSteps])
#Initialize angular frequency at 0.
omega1[0] = 0
omega2[0] = 0

#Iterate through the time steps, using the Euler-Cromer method to
#calculate and store the angular frequencies and thetas for each t+dt.
for n in range(1,numSteps):
    omega1[n] = omega1[n-1]-((g/l*sin(theta1[n-1])+q*omega1[n-1]+Fd*sin((2.0/3.0)*t[n-1])))*dt
    theta1[n] = theta1[n-1]+omega1[n]*dt

#Perform the same operation for theta2.
for m in range(1,numSteps):
    omega2[m] = omega2[m-1]-((g/l*sin(theta2[m-1])+q*omega2[m-1]+Fd*sin((2.0/3.0)*t[m-1])))*dt
    theta2[m] = theta2[m-1]+omega2[m]*dt


#Plot the difference between angles against time, taking the log of the
#difference
y = exp(0.049*t)*exp(-10**-5)
semilogy(t,(theta1 - theta2))
plot(t,y)
xlabel('Time [seconds]')
ylabel('Theta 1 - Theta 2 [radians]')
suptitle('Chaotic Behavior of Two Pendula - Delta Theta Versus Time')

show()
