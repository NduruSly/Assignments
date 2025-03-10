class Shape:
    def __init__(self):
        self.unit= "meters" #Example initialization
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
            super().__init__() #Inherits Shape's __init__
            self.length= length
            self.width= width

    def calculate_area(self):
        super().__init__() #Calls Shape's constructor again
        return self.length * self.width




