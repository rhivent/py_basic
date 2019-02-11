'''
type(2)  ==> hasilnya <class 'int'>
type('2')  ==> hasilnya <class 'str'>
ini menandakan semua tipe adalah object.

operator oveloading adalh operator dimana bisa menghandle
penggabungan 2 tipe data yg berbeda supaya tidak ada error.

jika 2+2 maka hasilnya 4
jika '2' + '2' maka hasilnya '22'
jika '2' * '3' maka hasilnya '222'
jika 2 * 3 maka hasilnya 6

jadi operator + is functionally diffently when diffent kind of data
jadi operator * is functionally diffently when diffent kind of data

in other words + (plus) atau *(asteric) operator is overloaded
utk handling diffent kind of object
'''

# contoh lainnya
import math

class Circle:
    def __init__(self,radius):
        self.__radius = radius

    def setRadius(self,radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2
    # provide 2 parameter utk adding oveloading
    def __add__(self,circle_objct):
        return Circle(self.__radius + circle_objct.__radius)
    def __lt__(self,circle_objct):
        # remove Circle utk menampilkan hasil True or False bukan hexadecimal
        return (self.__radius < circle_objct.__radius) # return nilai bolean(False or True)
    def __gt__(self,circle_objct):
        return (self.__radius > circle_objct.__radius) # return nilai bolean(False or True)
    def __str__(self):
        return "Circle area: " + str(self.area())

c1 = Circle(2)
c2 = Circle(3)

print(dir(c1)) #menampilkan method apa saja yg bisa dipakai dan method yg telah dibuat

# c1 + c2  #hasilny TypeError : unsupported operand.
# padahal pejelasan awal bisa antar class dengn tipe sama
# hal ini bisa diatasi dengan python operator overloading

c3 = c1 + c2

print(c1.getRadius()) # tampil : 2
print(c2.getRadius()) # tampil : 3
print(c3.getRadius()) # tampil : 5
print(c1<c2) # tampil : True
print(c1>c2) # tampil : False

print(str(c1))


'''
python operator overloading
Operator    expression      function
        Math Operator Overloading
   +         p1 + p2        p1 __add__(p2)
   -         p1 - p2        p1 __sub__(p2)
   *         p1 * p2        p1 __mul__(p2)
   **        p1 ** p2       p1 __pow__(p2)
   /         p1 / p2        p1 __truediv__(p2)
   //        p1 // p2       p1 __floordiv__(p2)
   %         p1 % p2        p1 __mod__(p2)
        Bitwise Operator Overloading
   <<        p1 << p2       p1__lshift__(p2)
   >>        p1 >> p2       p1__rshift__(p2)
  AND(&)     p1 & p2        p1__and__(p2)
  OR(|)      p1 | p2        p1__or__(p2)
  XOR(^)     p1 ^ p2        p1__xor__(p2)(+)
  NOT(~)     ~p1            p1__invert__()
        Comparison Operator Overloading
lessthan      p1<p2         p1__lt__(p2)
lessthan =    p1<=p2        p1__le__(p2)
equal to      p1==p2        p1__eq__(p2)
not equal to  p1!=p2        p1__ne__(p2)
greaterthan   p1>p2         p1__gt__(p2)
gt equal to   p1>=p2        p1__ge__(p2)
'''
