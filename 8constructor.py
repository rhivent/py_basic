'''
constructor yaitu fungsi yg dipanggil paling awal
dari semua fungsi lain dan nama fungsi contructor
tidak bisa diubah sudah default nama OOP dari python

def __init__(self):

ingat tambahkan self pada argumen constructor
sebagai instasiasi setiap fungsi yg ada di dlm class,
sebagai indikasi dari instasiasi dari class

bisa juga di tambahkan argumen pada constructor

__del__(self) utk menghapus class objek
__init__ akan selalu dipanggil jika membuat objek baru yg dlm class tsb
ada method ini.
'''
class Person:
    def __del__(self):
        print(self.id,'our class has been deleted!')
    def __init__(self,id):
        self.id=id
        print('our class has been created!')

    def setFullName(self,firstname,lastname):
        # inisiasi self sebagai indiki currrent objek
        # self bisa diganti nama lain abc, dqw, dll.
        # maka yg lain harus sama dengan nama argumen pertama
        # dalm hal ini kita menggunakan nama self
        self.firstname=firstname
        self.lastname=lastname
    def printfullname(self):
        print(self.firstname,self.lastname)
    def printname(self):
        print(self.firstname,self.lastname)
# berikan parameter/pada objek Person yg akan diberi ke constructor sebgai inisiator
personname = Person(5)
personname.__del__();
personname.setFullName('programming','language')
personname.printfullname()
personname.printname()

# contoh lain
class Car:
    def __init__(self,speed,color):
        print(speed)
        print(color)
        self.speed = speed
        self.color = color
        print('the __init__ is called')

ford = Car(200,'red')
honda = Car(200,'blue')

print(ford.speed)
print(ford.color)

class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width

rect1 = Rectangle(20,60)
rect2 = Rectangle(50,40)

print(rect1.height * rect1.width)
