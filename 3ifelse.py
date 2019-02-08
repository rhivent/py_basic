
#indentasi penting karena jika tidak ada tab/jarak saat eksekusi kode pada kondsi if maka akan muncul error
n = int(input("Number : "))
if n<0:
    print("The Absolute value of",n," is",-n)
else:
    print("Your value is",n)

name = input("Name?")
if name =="mark":
    print("valid name",name)
elif name =="john":
    print("valid name",name)
elif name =="mark":
    print("valid name",name)
elif name =="tom":
    print("valid name",name)
else:
    print("name is not valid",name)

#lihat indentasi pada kedua if, print
hewan = "animal"
animalName = "dogkwowkowk"
if hewan=="animal":
    if animalName=="dog":
        print('valid animalName')
    else:
        print(animalName,"invalid")
    print('valid hewan')
else:
    print('name not valid')
