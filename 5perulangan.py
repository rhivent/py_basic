a = 0
while a<5:
    print("the value of a is ",a)
    a+=1 #a=a+1
else:
    print("Finished while loop")

b = 1
c = 0
print('Enter number to add to the simple calculator')
print('enter 0 to quit')
while b != 0:
    print('current sum :',c)
    b = float(input("Number :"))
    b = float(b)
    c += b
    print ('Total is',c)
else:
    print("Finished sum")

# for utk mengulang, tuple, dictonary,list, set, string
q = [1,5,7,3,7,3,4,5,6,7,1,9,7,5]
# num ini adalah variabel yg dideklarasikan secara langsung yg mewakili nilai 1 by 1 dr var q =[...]
for num in q:
    print(num)

A = [0,1,2,3,4,5] # list
B = (0,1,2,3,4,5) # tuple
C = {0,1,2,3,4,5} # set
D = '012345'
E ={    #dictonary
    "name" : "max",
    "age" : 20
}

# menentukan apakah nilai yg kita input benar atau salah
print(100 in B)  # false krn angka 100 tidk ada di var B
print('123' in D)  # true krn angka 100 tidk ada di var D dst..

# menyimpan data yg ada di A di dlm x shg variabel x=A
for x in A:
    print(x)
for x in B:
    print(x)
for x in C:
    print(x)
for x in D:
    print(x)
for x in E.keys():
    print(x)
for x in E.values():
    print(x)
for key,value in E.items():
    print(key, '=',value)

# mengulang data 0 sampai kurang dari 6 ==> 0..5
for x in range(6):
    print(x)
# mengulang data dengn nilai awal 2, batas akhir angka 30 kemudian ada penambahan 3
for x in range(2,30,3):
    print(x)
    # muncul 2,5,...,29
else:
    print("Finished")
