# Design a class to represent a rectangle
# Some methods examples can be the
#rectangle area and rectangle perimeter.
import math
class Rectangle(object):
    def __init__(self,length, width):
        self.new_len = length
        self.new_width = width

    def area(self):
        total_area = self.new_width * self.new_len
        return total_area

    def perim(self):
        return (self.new_width + self.new_len) * 2

    def __str__(self):
        amount = self.new_len * self.new_width
        amount_p = (self.new_width + self.new_len) * 2
        return "area is cm" + str(amount) + "\n" + "perimeter is cm" + str(amount_p)

p1 = Rectangle(10,8)
print(p1)
