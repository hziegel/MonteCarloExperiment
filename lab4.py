from random import *
from math import *

# Monte Carlo method to find out approximate value of Pi using "Buffon Needle Experiment"

# pi ~ (2l*n)/th
length_pin = 1  # l = length of pin
number_tosses = 10000  # n = number of attempts
t_width = 2*length_pin  # t = width between lines
hits = 0  # h = hits of needles that cross lines

for i in range(number_tosses):
    angle = random()*(pi/2)
    position = random()*t_width
    # if 1/2 sin of theta >= d(distance of the center of the pin to the line), then hits
    if .5*sin(angle) >= abs(position-t_width):
        hits = hits + 1

print("The approximate value of pi is ", (length_pin*number_tosses)/(t_width*hits))