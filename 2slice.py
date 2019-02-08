mylist = [0,1,2,3,4,5,6,7,8,9]
print(mylist[4:8])
print(mylist[5:10])
print(mylist[5:])
print(mylist[:5])
print(mylist[-4:-2])
print(mylist[-6:])
print(mylist[:-6])
print(mylist[:])
print(mylist[::3])
print(mylist[0:10:3])
print(mylist[::2])
print(mylist[0:10:2])

# +--+--+--+--+--+--+--+
# |P| Y | T | H | O | N |
# +--+--+--+--+--+--+--+
# indexing dari awal : 0,1,2,3,4,5
# indexing dari akhir : -6,-5,-4,-3,-2,-1
# index dr akhir akan membuat urutan terbalik (reverse order)
print(mylist[::-2])
print(mylist[::-3])

names = ['a','b','c','d','e']
print(names[2:4])

# list
a = [0,1,2,3,4,5,6,7,8,9]
# tuple
b = (0,1,2,3,4,5,6,7,8,9)
c = '01239019301'

# Python slice
# a[start:end]    items start through end-1
# a[start:]       items start through the rest of the array
# a[:end]         items frmo the beginning through end-1
# a[:]            a copy of the whole array
# a[start:end:step]   start through not past end, by step

# x = slice(start,end,step)
x = slice(0,5)
# menampilkan slice pada variabel a
print(a[x])
# berdasarkan variabel itu sendiri
# tanda : adlah notasi dari slice()
print(a[0:5])
