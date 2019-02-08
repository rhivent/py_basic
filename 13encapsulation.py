class Car:
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color = color
    # Encapsulation fungsi setter
    def set_speed(self,value):
        self.__speed = value
    # Encapsulation fungsi getter
    def get_speed(self):
        return self.__speed
    # Encapsulation fungsi setter
    def set_color(self,value):
        self.__color = value
    # Encapsulation fungsi getter
    def get_color(self):
        return self.__color
ford = Car(200,'red')
honda = Car(200,'blue')

# change speed
# ford.speed = 300
# change speed dngn tipe string
# ford.speed = 'asdaf'
'''
maka bisa mmbuat ini tidak relevan, maka perlu proteksi
atas apa yg diinput type data nya. Encapsulation perlu
utk proteksi dari user yg ingin merubah data

cara Encapsulation yaitu membuat fungsi proteksi
utk membuat data private yaitu dngn membuat variabel
dngn __variabel (double underscore)
private variabel hanya bisa digunakan di dlm class itu sendiri,
jk digunakan di luar class maka akan error.
'''

ford.set_speed(300)
# shg kode utk merubah variabel tidak bisa
# maka ada error no attribut

print(ford.get_speed())
print(ford.get_color())
print(ford.__speed)
