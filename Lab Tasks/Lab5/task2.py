#Layyana Junaid 23k-0056 BSAI-3A
#task 2

class Shape:
    def area_of_shape(self):
        print("Area: ")


class Rectangle(Shape):
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

    def area_of_shape(self):
        return self.length * self.breath


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area_of_shape(self):
        return 0.5 * self.base * self.height


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area_of_shape(self):
        return self.length * self.length


rectangle = Rectangle(5, 3)
triangle = Triangle(4, 6)
square = Square(7)

print("Rectangle's area:", rectangle.area_of_shape())
print("Triangle's area:", triangle.area_of_shape())
print("Square's area:", square.area_of_shape())