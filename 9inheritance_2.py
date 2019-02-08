'''
python inheritance
=> Classes in python can be extended, creating new
classes which retain characteristics of the base class.
=> This process, known as inheritance.
=> Involves a superclass and a subclass.
=> The subclass inherits the  members of the  supercalss, on top which it can
add its own members.
'''
class Polygon:
    __width = None
    __height = None

    def set_values(self,width,height):
        self.__width = width
        self.__height = height
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height

class Rectangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height()


class Triangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height() / 2

rect = Rectangle()
tri = Triangle()

rect.set_values(50,40)
tri.set_values(50,40)
print(rect.area())
print(tri.area())
