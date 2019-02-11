'''
lambda function adalah anonymous function
dia tidak ada nama, atau hanya single line function atau functional programming

lambda argumen : proses argumen

contoh dibawah ini penggunaan fungsi lambda, dan dibandingkan dngn
fungsi biasa.

fungsi lambda digunakan utk:
digunakan ketika fungsi mengambil sebgai argument
atau return fungsi sebgai hasil tidak sebagai proses.

di dlm functional programming is a first class function artinya
kita bisa mempassing fungsi sebagai argumen. Atau me return function as function
thats why lambda fungsi useful.

lambda fungsi bisa digunakan pada filter, reduce or map function

1. map(function,iter1)
digunakan utk membuat object hexadecimal dengn 2 parameter, dan bisa diconversi
jadi map() mengaplikasikan tiap operasi fungsi ke dalam tiap
elemen yg ada di dlm parameter ke2

2. filter(function)
ada 2 parameter yg dimasukkan di dlm fungsi filter(), yg spesial dari filter()
adalah parameter pertama fungsi akan menghasilkan tipe data boolean.

3. reduce()
butuh import dari library reduce from functools
===>>> from functools import reduce

cara kerja reduce yaitu memproses argumen sesuai dengna operasi yg ada
contoh:
mylist = [1,2,3,4,5]
e = reduce(lambda x , y : x + y,mylist)
print(e) # hasilnya 15

hasil ini didpt dari argumen x = 1 , argumen y = 2 kemudian dioperasikan x+y
mendapat nilai 3. nilai 3 ini dijadikan oleh reduce sebagai argumen x kemudian
argumen y = 3 didapt dr nilai setelah 2 angka di list yaitu angka 3 kemudian
didapat nilai x+y = 6 dan dijadikan x, dan y = 4 , ditambah x+y =10, dijadikan
x , y = 5, ditambah 15.
'''
# def double(x):
#     return x *2
# def add(x,y):
#     return x + y
# def product(x,y,z):
#     return x * y * z

# fungsi diatas bisa disingkat dngn lambda keyword
# menyimpan fungsi di dlm masing2 variabel

from functools import reduce

double = lambda x : x * 2
add = lambda x, y :x + y
product = lambda x, y, z : x * y * z

print(double(10))
print(add(10,20))
print(product(10,20,30))

# map()

mylist = [1,2,3,4,5]
mylist2 = [2,4,6,8,10]
# tampung kedalm variabel
a = map(lambda x : x * 2,mylist)
# ini melakukan operasi fungsi yg ada di tiap elemen variabel mylist
print(a)
# hasilnya yaitu: <map object at 0x7fc6a9574cf8>
# conversi ke data tipe list
print(list(a))
# hasilnya yaitu: [2, 4, 6, 8, 10]


# membuat list dari penambahan elemen tiap list di mylist dan mylist2
b = map(lambda x,y:x+y, mylist,mylist2)
print(list(b))
# ini hasilnya penambahan tiap elemen mylist dan mylist2 : [3, 6, 9, 12, 15]



# filter()
# filter utk angka genap
c = filter(lambda x : x%2==0,mylist)
print(list(c)) # hasilnya : [2, 4] hal ini terjadi karena sisa hasil bagi 0 dan genap

# filter jika angka lebih dari 3
d = filter(lambda x : True if x > 3 else False, mylist)
print(list(d)) # hasilnya [4, 5] karena difilter sesuai kondisi jk angka > 3


# reduce()
e = reduce(lambda x , y : x + y,mylist)
print(e) # hasilnya 15
