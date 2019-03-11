# This is your coding interview problem for today.
#
# This problem was asked by Google.
#
# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
#
# Hint: The basic equation of a circle is x2 + y2 = r2.


# Solution Monte Carlo methods rely on random sampling. In this case, if we take a cartesian plane and inscribe a
# circle with radius r inside a square with lengths 2r, then the area of the circle will be πr2 while the area of the
# square will be (2r)2 = 4r2. Then, the ratio of the areas of the circle to the square is π / 4.
#
# So, what we can do is the following:
#
# Set r to be 1 (the unit circle) Randomly generate points within the square with corners (-1, -1), (1, 1), (1, -1),
# (-1, 1) Keep track of the points that fall inside and outside the circle You can check whether a point (x,
# y) is inside the circle if x2 + y2 < r2, which is another way of representing a circle Divide the number of points
# that fall inside the circle to the total number of points -- that should give us an approximation of π / 4.

from random import uniform


def generate():
    return uniform(-1, 1), uniform(-1, 1)


def is_in_circle(coords):
    return coords[0] * coords[0] + coords[1] * coords[1] < 1


def estimate():
    iterations = 10000000
    in_circle = 0
    for _ in range(iterations):
        if is_in_circle(generate()):
            in_circle += 1
    pi_over_four = in_circle / iterations
    return pi_over_four * 4
