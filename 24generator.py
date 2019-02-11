'''
generator adalah cara sederhana membuat iterator.
ketika menggunakan generator maka akan return iterator
objek.
fungsi yg ada 1 yield maka itu disebut fungsi generator

perbedaan yield dngn return
return : akan menghentikan proses pada fungsi dan mengembalikan
nilai, shg tidak bisa do somthing setelah ada keyword return di fungsi

yield: menutup fungsi dan menyimpan state dr fungsi

perbedaan iterator dngn generator, jika di dlm iterator
butuh implementasi __iter__() dan __next__()
sedangkan generator hanya perlu yield keyword

keuntungan memakai generator:
1. easy to implementasi
2. more efisien, dengan logic yg sama dngn __iter__ dngn fungsi normal
jika ada data jutaan maka akan di simpan 1 by 1, oleh yield
jika video maka di simpan setiap step dalam streaming video

'''
def my_func():
    yield 'a'
    yield 'b'
    yield 'c'

# assign fungsi my_func, dmn fungsi ini return iterator obj dan disimpan di dlm variabel x
x = my_func()

print(next(x)) # tampil a
print(next(x)) # tampil b
print(next(x)) # tampil c
# print(next(x)) # tampil exception StopIteration
def fungsi2():
    n = 1
    print('+++++++++',n)
    yield n
    n += 1
    print('+++++++++',n)
    yield n
    n += 1
    print('+++++++++',n)
    yield n

y = fungsi2()
print(next(y))
print(next(y))
print(next(y))
print('####################')

def fungsi3():
    for i in range(5):
        print('angka :',i)
        yield i

z = fungsi3()

print(next(z)) # tampil angka 0
print(next(z)) # tampil angka 1
print(next(z)) # tampil angka 2
print('####################')

# re create hole of class in 23iterator.py
def list_iterator(list):
    for i in list:
        yield i

a = [1,2,3,4,5,6,7]
# initial objk
mylist = list_iterator(a)

print(next(mylist)) # tampil nilai pertama d variabel a
print(next(mylist)) # tampil nilai kedua d variabel a
print(next(mylist)) # tampil nilai ketiga d variabel a

for b in mylist:
    print(b)
