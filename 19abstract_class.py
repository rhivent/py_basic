'''
abstract class itu semacam class templating,
dimana kita hanya mengakses method2,varibel2 yg
ada di dlm abstract class, dan kita tidak ingin menginstasiasi
class abstract karena hanya berisi interface/ template method
yg digunakan oleh Child class atau implement dari kelas lain
caranya membuat abstract class yaitu:
akses built-in module in python utk method abstract yaitu
dari ABC module, yaitu module built-in dari python utk abstract class

from abc import ABC, abstractmethod

ketika inherit dari ABC module maka perlu decorative dari
klass yg menggunakan ABC module

tiap method dibuat abstract dengan menambah @abstractmethod
di atas method yg ingin dijadikan abstract

ketika sudah ada abstract maka kita tidak bisa menginstasiasi
seperti cara biasa misal
shape = Shape() ==> akan terjadi error

utk subclass yg inherit dari superclass yg sudh di jadikan abstrak class
maka perlu mengdefinisika semua abstrak method di dlm subclass tersebut
jika tidak maka akan error krn subclass tidak mendefinisikan semua
method yg dilm abstrak kelas

Abstrak class harus mempunyai minimal 1 method abstrack
dan mengimport ABC module serti meninherit ABC module di dlm
class yg ingin dijadikan abstrak.
Method yg dijadikan abstrak harus ada decorative @abstractmethod
di atas method yg di deklarasikan/definisikan
'''
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Square(Shape):
    def __init__(self,side):
        self.__side = side
    def area(self):
        return self.__side * self.__side
    def perimeter(self):
        return self.__side * self.__side

square = Square(5)
print(square.area())
print(square.perimeter())
