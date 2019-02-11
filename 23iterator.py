'''
iterator is an object which can be used to iterate
over a collection.

__iter__() dan __next__()
'''

a = [1,2,3,4,5,6,7]
for i in a:
    print(i)

# dir(a)
'''
ketika mengkeksekusi kode dir(a) di scroll ke kanan ada listing
built-in function yg bisa digunakan utk proses data list
variabel a.
__iter__ juga ada di type data list, dictionary, tuple

fungsi __iter__ dan __next__ bisa dijadikan object, dipanggil bisa tanpa _ (underscore)
diawal atau diakhir

fungsi next() menampilkan bagin pertama dari data yg didlm varibel

'''
# akan membuat object iterator pada type data utk varibel a
test = iter(a)
# utk menampilkan data pertama dari iterasi
# dgn fungsi next()
next(test) # tampil angka 1
next(test) # tampil angka 2
next(test) # tampil angka 3
next(test) # tampil angka 4

'''
utk membuat iteration class maka perlu implementasi
__iter__() dan __next__()

fungsi next( hanya bisa dieksekusi dalam fungsi 1 kali)
jika dipanggil utk lebih dari 1 kali dalam 1 file, maka
akan reset saat dipanggil, sesuai dengan parameter list
atau variabel yg di passing didalam fungsi : next(param)
'''
class ListIterator:

    def __init__(self,list):
        # create member variabel
        self.__list = list
        # create index varibel
        self.__index = -1

    # impelement __iter__
    def __iter__(self):
        # memberi iterator
        return self

    # impelement __next__
    def __next__(self):
        # indexing tiap iterasi dari 0
        self.__index += 1
        # create exception ktika semua index telah diiterasi atau nilai index = panjang index
        if  self.__index == len(self.__list):
            # raise StopIteration
            raise StopIteration
        # memberi value/nilai saat ini, pada index skrng
        return self.__list[self.__index]

# a = [1,2,3,4,5,6,7]
# create object, n passing variabel a as argument di object
myList = ListIterator(a)
it = iter(myList)
print("################################################")
print(next(it)) # tampil 1
print(next(it)) # tampil 2
print(next(it)) # tampil 3
print(next(it)) # tampil 4
print(next(it)) # tampil 5
print(next(it)) # tampil 6
print(next(it)) # tampil 7
# print(next(it)) # exception StopIteration

print("################################################")
# bisa juga dengan for loop utk print tanpa menggunakan next()
# for b in it:
#     print(b)
