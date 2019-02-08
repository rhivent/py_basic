'''
python adalah
->multi-paradigm programming language
->interpreted language
->support dynamic data type
->independent from platforms
->focused on development time
->simple and easy grammar
->high-level internal object data types
->automatic memory management
->free(open source)

History
===================
=>Born(1989): name picked
=>by Guido van Rossum, now at dropbox
=> first public release (USENET) - feb 1991
=> python.org website - 1996 or 1997
=>Python software foundation-2001
=>Rossum chose the name "Python", since he was a big fan of
Monty Python's Flying Circus.

why learn python
=> fun to use ('scripting language')
=>OOP, imperative, functional programming and procedural styles
=>Highly educational
=>easy to learn, it runs on any platforms
=>powerful, scalable, easy to maintain : high productivity, lots of libraries
=>Glue language : interactive front-end for FORTRAN/C/C++ code

where to use python?
=> web development( django framework and flask for API)
=> DATA SCIENCE-including machine learning, daa analysis, dan data visualization
=>scripting : prototyping,etc.
=>GUI (graphic user interface), embedded applications, gaming, DevOps Tools
=>Education

Python operator Precedence
parentheses ==> ( ... )
exponents ==> **
multiplication and division ==> *,/,//,%
addtion and subtraction ==> +,-
'''

# variabel
# penamaan variabel : angka tidak didepan, tidak
# ada tanda . maupun spasi dan tidak boleh
# sama dngn reserved words(kata yg sudah ada) pada
# default python : contoh
# _varibel , var123,var_129
#
# angka
# int = 10
# float = 20.4
# complex = 1j
# num = 10e5
#
# ingin tau type data pada variable maka dengan fungsi
# type(variabel)


print("hello world!")
print(3*(4+5)-6/2)
myvariabel = 11

print(myvariabel +2)

# value = int(input("enter the value:"))
# value2 = float(input("enter the value:"))
#
# print(value +20)
# print(value2 +.09)

# perhitungan perpangkatan
print(pow(5,3))

# list fungsi built in pada python3
# print(dir(__builtins__))

#mengetahui suatu fungsi builtin degnan help()
# print(help(max))

#perhitungan panjang suatu string
print(len('namaku test testkqwokeoqkw asdmk'))

#perhitungan nilai terbesar suatu string
print(max(1,2,3,99,555,3332423,11231231,23123))

#menggunakan library math untuk perhitungan akar
import math
print(dir(math))
print(math.sqrt(25))
#dengan variabel
sqrroot = math.sqrt
print(sqrroot(9))

#input and print
x =int(input("input 1st number: "))
y =int(input("input 2nd number: "))
z =int(input("input 3rd number: "))

print ("The max of three values is :")
print(max(x,y,z))

input("Press ENTER to exit")

a = 'I\'m single quoted'
b = "I am a double quoted \"ehehe\""
c = 50
print(a)
print(b)
print(a+b)
print(a*c)
print(a+ str(c))

# array
names = ["mark", "ventus","july"]
print(names)
print(names[2])
print(names[-1])
# mengnambah kedalam list pada index ke 1 dengan angka 3
names.insert(1,3)
print(names)

# menambah elemen pada akhir list
names.append("test")
print(names)

# meremove element terakhir saja
names.pop()
print(names)

age = [12,11,123,14]
names.extend(age)
print(names)

names.remove(123)
print(names)
print(len(names))
print(names,age)

# sorting angka dari kecil ke besar
print(names.sort())
# sorting angka dari besar ke kecil
print(names.reverse())

# mengkopi data list
qwe = names.copy()
print(qwe)

# menghitung brp bnyk suatu elemen di dlm list
# jk tdk ada maka akan menampilkan angka 0
print(names.count("july"))

# mereset isi suatu list
z = [1,2,3,4]
z.clear()
print(z)

# delete list
del names
print(names)

var1 = 12
var2 = 10
print("{0} * {1} = {2}".format(var1,var2,var1*var2))
print('halo','dunia',sep="--")

# print dengan tanda modulus
# %s utk string
# %d utk angka decimal
# jika menggunakan ini maka kita harus
# menggunakan variabel yg dipassing nilainya contoh:

namaanda = 'max'
print('halo %s' %namaanda)
umuranada = 20
print('halo %s ! are you %d years old' %(namaanda,umuranada))

print('mark = %f' %92.5)
# utk membuat 2 angka dibelkng koma
print('mark = %.2f' %92.5)

tes1 = 'Halo'
tes2 = '  HALLO, WORLd '
print(tes1.islower())
print(tes2.isupper())
print(tes1.replace("H","O"))
print(tes2.split(','))

# boolean
# True utk benar , False utk salah jika menulis true
# maka python tidak mengenali dan terjadi error,
# karena case sensitive pada penamaan variable ataupun
# fungsi,
