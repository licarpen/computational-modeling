from pylab import *

N = 200
M = 50
data = zeros([N, N])

for i in range(N):
	# define real part of the function
	x = -2.0 + 3.0 * i / (N - 1.0)
	for j in range(N):
		# define imaginary part of the function
		y = -1.0 + 2.0 * j / (N - 1.0)
		# z_0 is a complex number defined by the values of x and y
		z_0 = complex(x, y)
		z = 0
		for m in range(M):
			# exclude values that diverge
			if (abs(z)>2):
				break
			z = z * z + z_0
		# include values that fall within desired range
		data[j, i] = 1.0 / m

imshow(data, cmap=cm.spectral, extent=[-2, 1, -1, 1])
colorbar()
show()
