from math import pi
copper = 1.678*10**(-8)
alluminium = 2.82*10**(-8)
def diameter(wire_gauge):
    d = 0.127 * 92 **((36-wire_gauge)/39)
    return d
d = diameter(wire_gauge)
def copper_wire_resistance(d):

    R = (4*copper*length)/(pi*diameter**2)
    return R
diameter(5)
copper_wire_resistance(35,diameter)


#not finisheddddddddddddd