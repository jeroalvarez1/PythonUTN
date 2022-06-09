import math

class AreaLength:
    def __init__(self, radius):
        self.radius = radius


    def operaciones(self):
        area = math.pi * self.radius ** 2
        area = "{0:.2f}".format(area)
        length = 2 * math.pi * self.radius
        length = "{0:.2f}".format(length)
        print(f"The area circle with a radius of {self.radius} is {area}")
        print(f"The circle length with a radius of {self.radius} is {length}")


radius = float(input("Type the circle radius: "))
llamarClase = AreaLength(radius)
llamarClase.operaciones()