'''
sets adalah unorder collection dgn tidak ada duplikasi
elemen dan no indexing

pembuatan variabel utk sets
variabel1 = {elemen1,elemen2,...}
atau
variabel2 = set((elemen1,elemen2,...))
atau
variabel3 = set([elemen1,elemen2,...])
'''

A = {1,2,3,4,5,2,5,3}
B = set(( "max",'saya','kamu'))
C = set(['qwe',1.4,12,11,'asd'])
D = {1,2,3,4,63,2,1,5,6,8,4}
print(A)
print(B)
print(C)
print(D)

# menggabungkan set dengn tanda | atau fungsi union()
print(A | B)
print(A.union(B))

# perpotongnan atau irisan atau elemen yg sama dimiliki kedua set
print(A & B)
print(A.intersection(B))

# mencari perbedaan antara 2 set
print(A - B)
print(A.difference(B))
print(B - A)
print(B.difference(A))

# perbedaan simetrik dari 2 set artinya kebalikan dari intersection
# yg mana yg tidak irisan di A dan B dngn cara tanda ^
print(A ^ B)
print(B ^ A)
print(A.symmetric_difference(B))

# set tidak terindeksi seperti list atau tuple
# misal A[0] maka error
# list alternatif method yg bisa digunakan utk set
# yaitu dengn cara dir(A)
print(dir(A))

print(len(A))

A.add(10)
print(A)

# utk menambah lebih dari 1 elelem ke dlm sets
A.update([12,13,11,521])
print(A)

A.remove(521)
print(A)

A.discard(12)
print(A)

# perbedaan discard() dan remove() yaitu ketika kita
# menghapus elemen yg tidak ada di dlm sets maka
# jk menggunakan remove() akan terjadi error sedngkan
# discard() tidak ada error.

# delete elemen terakhir pada sets
A.pop()
print(A)

# mereset isi set menjadi kosong
A.clear()
print(A)

# delete sets
del A
print(A)
