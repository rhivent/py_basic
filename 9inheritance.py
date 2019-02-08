'''
inheritance, subclasses, superclasses

inheritance memperbolehkan kita utk mendefinisikan
class dari klas yg utama/parent/class lain.
sehingga kita bisa membuat dan memaintain
aplikasi. Artinya kita bisa membuat kelas utama
kemudian kelas turunannya hanya perlu didefinisikan
sebagai anak kelas dari kelas utama. Dan anak kelas
dapat memakai fungsi2 atau variabel yg ada di kelas
utama.

jika ingin kelas anak tidak ingin ada apa2 hanya
menginisiasi sebagai anak kelas utama maka harus
menggunakan keyword : pass

inisiasi kelas anak tidak harus menginisiasi
kelas utama, asalkan sudh mengheritance dr kelas utama

dalam hal ini kelas anak bisa mejadi turunan
dari banyak kelas parent (multiple inheritance)
dgn pemisahan tanda , antar kelas
'''
class Parent:
    variabel1 ="this is var 1"
    variabel2 ="this is var 2"
class Parent2:
    variabel1 ="this is var 1"
    variabel2 ="this is var 2"
# ini cara menggunakan => class anak(kelas_utama):
class Child(Parent,Parent2):
    pass

# menginisiasi class degn menampung dlm variabel
# parent_ = Parent()
# print(parent_.variabel1)

# inisiasi anak kelas dengan ditampung variabel child_
child_ = Child()
# menggunakan variabel pada kelas utama
print(child_.variabel2,child_.variabel1)
