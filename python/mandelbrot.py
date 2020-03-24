from pylab import *

N = 200
M = 50
#define numbers for range

data = zeros([N,N])
#create matrix/array for data

for i in range(N):
	x = -2.0 + 3.0*i/(N-1.0);
#defining the real part of the function
	for j in range(N):
		y = -1.0 + 2.0*j/(N-1.0);
#defining the imaginary part of the function
		z0 = complex(x,y)
#making z_0 a complex number defined by the values of x and y
		z = 0
#starting at z = 0
		for m in range(M):
			if (abs(z)>2):
				break
#excluding values that sum to infinity
			z = z*z + z0
		data[j,i] = 1.0/m
#including values that fall within the range desired

imshow(data,cmap=cm.spectral,extent=[-2,1,-1,1])
#showing data in spectral color scheme and setting coordinate bounds
colorbar()
#including a color bar
show()
#show us the image!
