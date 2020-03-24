import pi from '../assets/pi.png';
import mandelbrot from '../assets/mandelbrot.png';

export const models = [
  {
    title: 'Archimedes\' Pi Approximation',
    image: pi,
    description: 'This script approximates the value of pi to 3 decimals using Archimedes\' method. The perimeters of two polygons are calculated, with one polygon circumscribed about a circle and the other inscribed in the same circle.  The outer perimeter is n * tan(theta/2.0), where theta is the inscribed angle in radians. The inner perimeter is defined as n * sin(theta/2.0).  As n increases, the difference between the two values will become less than 1.0E-4, resulting in pi to a precision of 3 decimals. The script prints a list of values using modulo to ensure consistency and equal column widths.'
  },
  {
    title: 'Mandelbrot Set',
    image: mandelbrot,
    description: 'This script generates the fractal pattern known as the Mandelbrot set.  The set displays characteristics of the set of complex, quadratic polynomials of the form f(z) = z^2 + c.  For each value of c, the sequence [0, f(0), f(f(0)), f(f(f(0)))...] is generated.  If this sequence does not diverge, the value of c is plotted.',
    script: ''
  }
];
