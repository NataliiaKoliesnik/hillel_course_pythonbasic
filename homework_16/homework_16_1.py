# work using class methods, dunder methods, and decorators — creating a Rectangle class

class NotRectangleException(Exception):
    pass

def validate_rectangle(func):
    def wrapper(self, other):
        if not isinstance(other, Rectangle):
            raise NotRectangleException(f'{type(other)} is not Rectangle')
        return func(self, other)
    return wrapper

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @validate_rectangle
    def __eq__(self, other):
        return self.get_square() == other.get_square()

    @validate_rectangle
    def __add__(self, other):
        new_square = self.get_square() + other.get_square()
        return Rectangle(new_square, 1)

    def __mul__(self, n):
        new_square = self.get_square() * n
        return Rectangle(new_square, 1)

    def __str__(self):
        return f'Rectangle with width {self.width} and height {self.height}'

    def get_square(self):
        return self.width * self.height


r1 = Rectangle(2, 4)
print(r1)
r2 = Rectangle(3, 6)
print(r2)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
print(r3)
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
print(r4)
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'