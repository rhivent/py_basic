# Comparison Operators:
# operator function
# < less than
# <= less than or equal to
# > greater than
# >= greater than or equal to
# == equal
# != not equal

# Logical Operators:
# and (A and B) is True jika kedua A dan B bernilai benar
# or (A or B) is True jika kedua A atau B bernilai benar
# not (A not B) jika kondisi benar maka logika operator not akan membuat false
# artinya kebalikan dari nilai sesungguhnya

if 9<10:
    print("true")
else:
    print("false")
if 9<=10:
    print("true")
else:
    print("false")
if 9>10:
    print("true")
else:
    print("false")
if 9>=10:
    print("true")
else:
    print("false")
if 9==10:
    print("true")
else:
    print("false")
if 9!=10:
    print("true")
else:
    print("false")

if 9<10 and 9!=10:
    print("true")
else:
    print("false")

if 9<10 or 9!=10:
    print("true")
else:
    print("false")


kata = "qwerty"
print("a" in kata)
print("qw" in kata)
print("qe" in kata)

a = [1,2,3]
b = [2,3,4]
c = [1,2,3]

print(a is b)
# variabel a dan c berbeda karena pendeklarasian kita di memori variable a memiliki unik sendiri, var b juga uniq
print(a is c)

c=d=[3,2,1]
# variabel ini dideklarasikan true karena ada tanda perbandingan
print("end this",c is d)
