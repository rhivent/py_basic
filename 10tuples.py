'''
tuple adalah mirip dengn list yg bisa menyimpan
koleksi dari elemen di dalam 1 variabel, tetapi
tuple jika sudah dibuat maka memiliki sifat immutable
artinya sekali dibuat tidak bisa dimodifikasi isi tuple,


'''
#  tuple menggunakan () sebagai penyimpan data instead
# of list used []
x = (1,2,3,4,5,6,7,7,8)
y = (1,'max',1.4)
print(x)
print(y)

print(min(x))
print(max(x))
print(x.count(7))
print(len(x))

# concatenation operator adalah tanda +
z = x + y
print(z)

# delete tuple
del z
print(z)

# contoh lain
a = ('hi',)*5
print(a)
print(a[2])
