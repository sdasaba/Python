class Shape:
    def __init__(self,w,l):
        self.width=w
        self.len=l
    
    def print_size(self):
        print('{} by {}'.format(self.width, self.len))


class Square(Shape):
    def area(self):
        return self.width * self.len

my_shape = Shape(20,25)
my_shape.print_size()

a_square = Square(20,20)
print(a_square.area())

a_square = Square(20,20)
print(a_square.print_size())