# Chaotic Behavior of Pendula
#Author: Lisa Carpenter

'''Abstract: A driven and damped pendulum will exhibit chaotic behavior if
initial conditions are set appropriately. The chaotic behavior is investigated
by modeling the behavior of two pendula with slightly different initial
conditions. The value for theta as a function of time for a driven/damped pendulum
is determined by using the Euler-Cromer method.  When log(delta_theta) is plotted 
against t, chaotic behavior will be evident for small time scales, and delta_theta 
increases linearly with time.  This is indicative of a chaotic system. Because the 
semi-log y plot shows a linear trend, delta_theta = exp[lambda*t), where lambda is 
the slope of the semi-log graph, and lambda is a parameter called the Lyapunov Exponent.  
This parameter is characteristic of chaotic behavior.  The Lyapunov Exponent for this
behavior is determined visually to be around 0.0039, with a y-intercept of 1E-05.  
When the Lyapunov Exponent changes sign, the chaotic regime has been met, which is 
confirmed by this model.'''

from pylab import *

# initialize gravity, pendulum length, damping q, end time, dt, and driving force Fd
g = 9.81
l = 9.81
q = 0.5
t_end = 120.0
dt = 0.01
Fd = 1.2
numSteps = int(t_end / dt)
t = arange(0.0, t_end, dt)
theta1 = zeros([numSteps])
theta2 = zeros([numSteps])
# initialize thetas for pendula to differ by 0.001
theta1[0] = 0.2
theta2[0] = 0.201
# angular frequency, omega, is used to calculate subsequent values of theta1 and theta2
omega1 = zeros([numSteps])
omega2 = zeros([numSteps])
omega1[0] = 0
omega2[0] = 0

# apply Euler-Cromer method to model omegas and thetas
for n in range(1, numSteps):
    omega1[n] = omega1[n - 1]-((g / l * sin(theta1[n - 1]) + q * omega1[n - 1] + Fd * sin((2.0 / 3.0) * t[n - 1]))) * dt
    theta1[n] = theta1[n - 1] + omega1[n] * dt

for m in range(1, numSteps):
    omega2[m] = omega2[m - 1] - ((g / l * sin(theta2[m - 1])+q * omega2[m - 1] + Fd * sin((2.0 / 3.0) * t[m - 1]))) * dt
    theta2[m] = theta2[m - 1] + omega2[m] * dt
    
y = exp(0.049*t)*exp(-10**-5)
semilogy(t,(theta1 - theta2))
plot(t,y)
xlabel('Time [seconds]')
ylabel('Theta 1 - Theta 2 [radians]')
suptitle('Chaotic Behavior of Two Pendula - Delta Theta Versus Time')

show()
