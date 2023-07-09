from cmath import pi
import math

def area(radius):
    Area = pi * (radius ** 2)
    return Area

radii = [10, 5, 8, 3, 7, 2.5, 8.7, 6.2, 9, 15]

for r in radii:
    areaa = area(r)
    print(f"The area of {r}meters radius circle is {areaa}square meters")