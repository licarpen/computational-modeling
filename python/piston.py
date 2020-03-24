from pylab import *

numdt = 1000 #number of time steps
v = zeros([100,2*numdt])
p = zeros([101,2*numdt])
dx = 0.02
rho = 1.5
c = 343.0
dt = dx/c
v_0 = 100.0
Z = 6000.0
f = 300.0

for n in range(0,numdt-1):
    for i in range(0,98):
        v[i+1,2*n+1] = v[i+1,2*n-1] - dt/(rho*dx)*(p[i+1,2*n] - p[i,2*n])
    v[0,2*n+1] = v_0*sin(2.0*pi*f*(2*n+1)*dt)
    v[-1,2*n+1] = 1.0/(1.0+Z*dt/rho/dx)*((1.0 - Z*dt/rho/dx)*v[-1,2*n-1]+2.0*dt/rho/dx*p[-2,2*n])
    for i in range(1,99):
        p[i,2*(n+1)] = p[i,2*(n-1)] - rho*c**2.0*dt/dx*(v[i+1,2*n+1] - v[i,2*n+1])
    p[-2,2*(n+1)] = p[-3,2*(n+1)]
    scatter(2*n,p[-4,2*n])

show()


