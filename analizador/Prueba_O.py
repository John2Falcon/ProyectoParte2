class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)
    def f1(self, x, y):
        return min(x, x+y)


# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g