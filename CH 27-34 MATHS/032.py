"""
032
Ask for the radius and the depth of a cylinder
and work out the total volume (circle
area*depth) rounded to three decimal
places.
"""
import math

radius = float(input("Enter the radius of the cylinder: "))
depth = float(input("Enter the depth of the cylinder: "))

area = math.pi * radius * radius
volume = area * depth
print(round(volume, 3))

