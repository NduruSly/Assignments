class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14159 * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length= length
        self.width= width
    def calculate_area(self):
        return self.length*self.width

def total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)

