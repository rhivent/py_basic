'''
self ini adalah menunjukkan class dirinya sendiri
seperti this pada PHP, JS. Shg argument ini secara
default harus di tulis jika kita menggunakan fungsi
yang menampung parameter fungsi yg ada di dalam kelas

hal ini ditunjukkan firstname,lastname adlh argumen
yang di process tetapi self sendiri tidak di process
tetapi sebagai default argument pada fungsi di dlm kelas
'''
class Person:
    def setFullName(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def printfullname(self):
        print(self.firstname,self.lastname)

''' inisiasi menjadi objek dengan menggunakan variabel
sebagai penampung objek
'''
personname = Person()
personname.setFullName('programming','language')
personname.printfullname()

class Car:
    # keyword pass artinya untuk menginisiai empty atau
    # tidak ada data/method di dlm class atau method
    pass

# instance class mjd object
ford = Car()
honda = Car()
audi = Car()

# bisa melakukan associate data ke object
ford.speed = 200
honda.speed = 220
audi.speed = 250
# speed disini dinamakan atribut
# ketika membuat empty class dngn pass keyword
# bisa menyimpan attribut apa saja di dlm class tsb

ford.color = 'red'
honda.color = 'blue'
audi.color = 'black'

print(ford.speed)
print(ford.color)

# changing speed atribut
ford.speed = 300
ford.color = 'blue'

print(ford.speed)
print(ford.color)

# jadi speed and color is variabel yg menampung data

# contoh lain
class Rectangle:
    pass
rect1 = Rectangle()
rect2 = Rectangle()

rect1.height = 20
rect2.height = 30

rect1.width = 40
rect2.width = 10

print(rect1.height * rect1.width)
print(rect2.height * rect2.width)
