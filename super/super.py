'''
creating superclass in python

super function is built-in function which
return approxy object that allow us refer us to
use super class dlm hal ini class Parent adalah
superclass
'''
class Parent1:
    def __init__(self,name):
        print('parent1 __init__',name)
class Parent2:
    def __init__(self,name):
        print('parent2 __init__',name)

class Child(Parent1,Parent2):
    def __init__(self):
        print('Child __init__')
        # create super function, artinya mengakses __init__ method dr class Parent
        # pass 1 argumen utk arg name pada class Parent
        super().__init__('dngn super function')

        Parent1.__init__(self,'tom')
        Parent2.__init__(self,'max2')

child = Child()
# maka yg dieksekusi yaitu constructor pd class Child
print(Child.__mro__)
'''
# menampilkan order
# mro = method resolution order
# ini adalah order yg di panggil di dlm class Child
# cara ekseskusinya yaitu dari class diri sendiri dulu
# kemudian Parent1 ,kemudian Parent2, kemudian class object
# itu adalah rule/aturan
jadi yg ada di dalam kelas Parent2 baik method dan parameter
akan dieksekusi setelah semua yg ada di dlm kelas Parent1
telah dieksekusi.

utk superclass bisa dilihat bahwa nilai yg dieksekusi
pada multi inheritance di dlm super() ternyata Parent1
sdngkan Parent2 tidak dieksekusi walaupun sama2 super class
dan memiliki __init__ method

solusi dari hal ini yaitu
memanggil secara manual tidak menggunakan fungsi default super()
contoh:
Parent1.__init__(self,'max')
Parent2.__init__(self,'max2')
'''
