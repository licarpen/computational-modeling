import pi from '../assets/pi.png';
import mandelbrot from '../assets/mandelbrot.png';
import radioactive from '../assets/radioactive.png';

export const models = [
  {
    title: 'Archimedes\' Pi Approximation',
    image: pi,
    description: 'This script approximates the value of pi to 3 decimals using Archimedes\' method. The perimeters of two polygons are calculated, with one polygon circumscribed about a circle and the other inscribed in the same circle.  The outer perimeter is n * tan(theta/2.0), where theta is the inscribed angle in radians. The inner perimeter is defined as n * sin(theta/2.0).  As n increases, the difference between the two values will become less than 1.0E-4, resulting in pi to a precision of 3 decimals. The script prints a list of values using modulo to ensure consistency and equal column widths.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/pi.py'
  },
  {
    title: 'Mandelbrot Set',
    image: mandelbrot,
    description: 'This script generates the fractal pattern known as the Mandelbrot set.  The set displays characteristics of the set of complex, quadratic polynomials of the form f(z) = z^2 + c.  For each value of c, the sequence [0, f(0), f(f(0)), f(f(f(0)))...] is generated.  If this sequence does not diverge, the value of c is plotted.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/mandelbrot.py'
  },
  {
    title: 'Euler Method Error for Radioactive Decay',
    image: radioactive,
    description: 'An analytical solution for radioactive decay is well known and can be used to determine the number of atoms left in a radioactive mass after a period of time. This script models the error in the Euler method as a function of the time step (dt) used in the Euler approach. Error as a function of dt is plotted by comparing the difference between the numerical values and each analytical value to the time step used.  In analyzing the plot of error versus dt, it appears that error as a function of dt is linear.  The error per step is actually dt^2. However, throughout the entire Euler calculation, t/dt time steps are used, and thus the error is proportional to the product of these two values - (dt^2) * t/dt =~ dt.  Thus, as time step increases, the error increases linearly as well.',
    script: 'https://github.com/licarpen/computational-modeling/blob/master/python/radioactive_euler.py'
  }
];
