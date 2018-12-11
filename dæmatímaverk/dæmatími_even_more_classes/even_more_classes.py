import math
class Circle:
    def __init__(self, radius):
        self.__radius = float(radius)

    
    def __str__(self):
        return "Area: {:.2f}\nPerimeter: {:.2f}".format(self.area(), self.perimeter())

    
    def area(self):
        return math.pi * self.__radius**2

    
    def perimeter(self):
        return 2 * math.pi * self.__radius


    def get_radius(self):
        return self.__radius

    
    def set_radius(self, new_radius):
        self.__radius = new_radius


def main():   
    radius = input("Radius of circle: ")        
    circle = Circle(radius)
    print(circle)
    circle.set_radius(circle.get_radius() + 1.0)   
    print(circle)

main()