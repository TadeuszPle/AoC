from math import floor, sqrt, ceil
with open('input.txt') as f:
    lines = f.readlines()
time, distance = lines
time = int(time.split(':')[1].replace(' ', ''))
distance = int(distance.split(':')[1].replace(' ', ''))
# equation x(time-x)>distance
# -x^2 -tx -d > 0
# x^2 +tx +d < 0
# delta = t^2-4(-1*-d) = t^2-4d
delta = time**2 - 4*distance
# solutions (-b +- delta)/2a
x1 = (-time-sqrt(delta))/-2
x2 = (-time+sqrt(delta))/-2

minimum, maximum = ceil(x2), floor(x1)
print(x1,minimum, x2, maximum)
print(maximum - minimum+ 1)