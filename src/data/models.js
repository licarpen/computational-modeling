import pi from '../assets/pi.png';

export const models = [
  {
    title: 'Archimedes Pi Approximation',
    image: pi,
    description: 'This script approximates the value of pi to 3 decimals using Archimedes\' method. The perimeters of two polygons are calculated, with one polygon circumscribed about a circle and the other inscribed in the same circle.  The outer perimeter is n * math.sin(math.radians(theta/2.0)), where theta is the inscribed angle, 360/n.  The inner perimeter is defined as n * math.tan(math.radians(theta/2.0)).  As n increases, the difference between the two values will become less than 1.0E-4, resulting in pi to a precision of 3 decimals. The script prints a list of values using modulo to ensure consistency and equal column widths.'
  }
];
