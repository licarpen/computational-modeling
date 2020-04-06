import pi from '../assets/pi.png';
import mandelbrot from '../assets/mandelbrot.png';
import radioactive_euler from '../assets/radioactive_euler.png';
import radioactive_rk from '../assets/radioactive_rk.png';
import prism from '../assets/prism.png';
import chaos_pendula from '../assets/chaos_pendula.png';
import knuckleball from '../assets/knuckleball.png';
import quadrature from '../assets/quadrature.png';
import randomwalk from '../assets/randomwalk.png';
import guitar from '../assets/guitar.png';
import noise from '../assets/noise.png';
import pyro from '../assets/pyro.png';
import logistic from '../assets/logistic.png';
import piSmall from '../assets/pi_small.png';
import mandelbrotSmall from '../assets/mandelbrot_small.png';
import radioactive_eulerSmall from '../assets/radioactive_euler_small.png';
import radioactive_rkSmall from '../assets/radioactive_rk_small.png';
import prismSmall from '../assets/prism_small.png';
import chaos_pendulaSmall from '../assets/chaos_pendula_small.png';
import knuckleballSmall from '../assets/knuckleball_small.png';
import quadratureSmall from '../assets/quadrature_small.png';
import randomwalkSmall from '../assets/randomwalk_small.png';
import guitarSmall from '../assets/guitar_small.png';
import noiseSmall from '../assets/noise_small.png';
import pyroSmall from '../assets/pyro_small.png';
import logisticSmall from '../assets/logistic_small.png';

export const models = [
  {
    title: 'Potential Surrounding Hollow Cube',
    image: prism,
    imageSmall: prismSmall,
    description: 'This script models the potential surrounding a hollow cube of potential V = 1, with the potential approaching 0 at large distances from the center of the cube.  The model makes use of the Jacobi method, which is a relaxation method for solving the 2nd order differential equation which describes the solution for given parameters.  Laplace\'s equation is used to relate the potential at a point relative to the potentials nearby. The Jacobi method is used to iterate through a matrix of potentials in a plane decreasing dv until the solution ceases to change by more than a chosen epsilon. At this point the potential is said to be relaxed. A spectral map is used to display the data.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/prism.py'
  },
  {
    title: 'Density of Knuckleball Placement',
    image: knuckleball,
    imageSmall: knuckleballSmall,
    description: 'A knuckleball is a pitch thrown in baseball that minimizes spin on the ball, resulting in an erratic trajectory.  This script models a knuckleball with a spectral map showing probabilistic spatial coordinates for when the ball reaches the batter\'s strike zone.  This is accomplished by using Newtonian Mechanics to describe the trajectory and using the Euler method to iterate through time steps to determine the placement of the ball in the z and y directions. A histogram (not shown) displays the probability that a knuckleball will strike a particular box the size of a baseball at the strike zone.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/knuckleball.py'
  },
  {
    title: 'Chaotic Behavior of Pendula',
    image: chaos_pendula,
    imageSmall: chaos_pendulaSmall,
    description: 'A driven and damped pendulum will exhibit chaotic behavior for a set of initial conditions. The chaotic behavior is investigated by modeling the behavior of two pendula with slightly different initial conditions. The value for theta as a function of time for a driven/damped pendulum is determined by using the Euler-Cromer method.  When log(delta_theta) is plotted against t, chaotic behavior will be evident for small time scales, and delta_theta increases linearly with time.  This is indicative of a chaotic system. Because the semi-log y plot shows a linear trend, delta_theta = exp(lambda*t), where lambda is the slope of the semi-log graph, and lambda is a parameter called the Lyapunov Exponent. This parameter is characteristic of chaotic behavior.  The Lyapunov Exponent for this behavior is determined visually to be around 0.0039, with a y-intercept of 1E-05. When the Lyapunov Exponent changes sign, the chaotic regime has been met, which is confirmed by this model.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/prism.py'
  },
  {
    title: 'Mandelbrot Set',
    image: mandelbrot,
    imageSmall: mandelbrotSmall,
    description: 'This script generates the fractal pattern known as the Mandelbrot set.  The set displays characteristics of the set of complex, quadratic polynomials of the form f(z) = z^2 + c.  For each value of c, the sequence [0, f(0), f(f(0)), f(f(f(0)))...] is generated.  If this sequence does not diverge, the value of c is plotted.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/mandelbrot.py'
  },
  {
    title: 'Displacement of Guitar String',
    image: guitar,
    imageSmall: guitarSmall,
    description: 'This script models the displacement of a string after it is plucked at 1/2 and 2/3 of the string length. Known equations for y displacement and velocity of a wave traveling on a string are used given parameters of string tension, density, initial displacement, and length. Frequency spectrum at 90% of string length is also generated (not shown). Fast Fourier Transforms are used to identify resultant frequencies.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/guitar.py'
  },
  {
    title: 'Logistic Bifurcation Diagram',
    image: logistic,
    imageSmall: logisticSmall,
    description: 'This program displays a bifurcation diagram mapping the logistic equation against the parameter mu. The logistic equation is defined iteratively as x_n+1 = mu * x_n (1 - x_n). For each value of mu, transient behavior of the logistic equation is eliminated and values of x_n are recorded. Chaos onset and period doubling are denoted on the diagram.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/logistic.py'
  },
  {
    title: 'Archimedes\' Pi Approximation',
    image: pi,
    imageSmall: piSmall,
    description: 'This script approximates the value of pi to 3 decimals using Archimedes\' method. The perimeters of two polygons are calculated, with one polygon circumscribed about a circle and the other inscribed in the same circle.  The outer perimeter is n * tan(theta/2.0), where theta is the inscribed angle in radians. The inner perimeter is defined as n * sin(theta/2.0).  As n increases, the difference between the two values will become less than 1.0E-4, resulting in pi to a precision of 3 decimals. The script prints a list of values using the modulo operator to ensure consistency and equal column widths.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/pi.py'
  },
  {
    title: 'Error in Euler Method for Radioactive Decay',
    image: radioactive_euler,
    imageSmall: radioactive_eulerSmall,
    description: 'An analytical solution for radioactive decay is well known and can be used to accurately predict the number of atoms left in a radioactive mass after a period of time. This script models the error in the Euler method as a function of the time step (dt) used in the Euler approach. Error as a function of dt is plotted by comparing the difference between the numerical values and each analytical value to the time step used.  In analyzing the plot of error versus dt, error as a function of dt exhibits linear behavior.  The error per step is actually dt^2. However, since t/dt time steps are used, the error is proportional to the product of these two values - (dt^2) * t/dt ~= dt.  Thus, as time step increases, the error increases linearly.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/radioactive_euler.py'
  },
  {
    title: 'Error in Euler-Comer Method for Radioactive Decay',
    image: radioactive_rk,
    imageSmall: radioactive_rkSmall,
    description: 'An analytical solution for radioactive decay is well known and can be used to accurately predict the number of atoms left in a radioactive mass after a period of time. This script uses the Euler-Cromer method for numerically calculating the error in radioactive decay number of atoms versus the time step.  The Euler-Cromer method differs from the well-known Euler method in that it uses the computed values of omega to compute the next iteration and uses a half-time step for more accuracy.  Error increases quadratically as dt increases, but the accuracy of the model is much higher for low values of t.  Error is proportional to the order of the time step multiplied by t/dt.  Since higher-order terms are present, the error will be of order (dt)^3*t/dt ~= (dt)^2, which is why a quadratic correlation between error and time step is observed.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/radioactive_rk.py'
  },
  {
    title: 'Random Walk in 1D',
    image: randomwalk,
    imageSmall: randomwalkSmall,
    description: 'This script models a random walk in 1D.  L particles step 1 unit left or right at random, with equal probabilities of each.  Steps are repeated for each particle n times.  A periodic boundary condition is applied, upon which particles that hit the boundary are positioned at the opposite end of the boundary. A histogram displays the ending location of each particle with respect to the starting point. A 1D random walk is often used as a starting point to demonstrating gaussian distributions, the behavior of gas particles in a container (which is the foundation of thermodynamics), and brownian motion.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/probwalk.py'
  },
  {
    title: 'Integral Approximation Techniques',
    image: quadrature,
    imageSmall: quadratureSmall,
    description: 'This script calculates the integral from -1 to 1 of the fucntion f(x) = x^2/cosh(x) in three different ways.  A bruteforce Monte Carlo technique is used, generating random numbers (x_i) in the interval from -1 to 1 and summing N rectangles of height f(x_i) and width 2/N to approximate the integral. The second method approximates each interval as a trapezoid and uses the boundaries of the function as h_1 and h_2 of the trapezoid. Finally, importance sampling is used to flatten the function, eliminating random values of x_i via the rejection method for the function p(x) = 1/cosh(x). The remaining x_i values are used with bruteforce to approximate the integral. The integral estimations are calculated for several values of N and presented in a table. The error in the importance and bruteforce MC method increases as 1/sqrt(N), where N is the number of samples used to calculate the integral. This can be shown by graphing error versus 1/sqrt(N).  The resulting correlation appears linear. While the trapezoid method of integration results in a precise result with N = 100, the MC techniques scale better in higher dimensions and require less computation for increased accuracy.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/quadrature.py'
  },
  {
    title: 'White Noise Generator',
    image: noise,
    imageSmall: noiseSmall,
    description: 'This script generates a white noise power spectrum using the Box-Muller method.  An array of 2^10 random numbers is generated and treated like a time series.  Fast Fouriert Transform (FFT) is used to compute the power spectrum of these values.  The Box-Muller method uses a Gaussian distribution with mean mu = 0 and sigma^2 = 1.  This probability distribution is then inverted to find the function from which to draw random numbers to represent the frequencies in white noise',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/noise.py'
  },
  {
    title: 'Pyrochlore Lattice',
    image: pyro,
    imageSmall: pyroSmall,
    description: 'This script models the structure of the Pyrochlore Lattice. This is done by defining a set of arrays representing basis vectors for both position in the coordinate system and position of the four atoms at each position.  While the points are generated, they are added to a 500*3 dimensional array.  The array is used to plot all of the atom positions in scatterplots showing views from the xy, yz, and zx planes.The data is written to a pyrochlore.dat file.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/pyro.py'
  }
];
