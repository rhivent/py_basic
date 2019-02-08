'''
seperti php, json, js, dll
python ada penamaan ttg associatif list atau map dengan
ada key : value pairs dipisahkan dngn tanda ,
dan di dlm {key:value , ...}

dengan key bisa apa saja data typenya dan valuenya bisa apa saja
data typenya
'''

D = { 'name':'max','age':24}
print(D)
# menampilkan value sesuai dengn key
print(D['name'])
print(D['age'])

E = {'name':'tom',14:12,13.4:14.2,True:True,(2,3):5}
# menampilkan data value dari key dengn data tipenya tuple
print(E[(2,3)])
# menampilkan data value dari key dengn data tipenya boolean
print(E[True])

# panjang dari dictonary
print(len(E))

# mengambil data berdasarkan key
D.get('name')

# add key:valuenya
D['surname'] = 'Nice'
print(D)

#menghapus berdasarkan key
D.pop('surname')
print(D)

# mereplace value berdasarkan key
D['name'] ="tom"
print(D)

# mengedit data berdasarkan key
D.update({'name':'max'})
print(D)

# menampilkan key apa saja yg ada dlm dictonary
print(D.keys())

# menampilkan value apa saja yg ada dlm dictonary
print(D.values())

# menampilkan item(key,value) apa saja yg ada dlm dictonary
print(D.items())

# menghapus item
D,popitem()
print(D)
