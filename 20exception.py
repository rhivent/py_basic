'''
exception handling adalah is an event, which occurs during
the execution of a program, that disrupts the normal flow
of the program.
artinya exception adalah exceptional event yg beda dari
yg dideklarasikan

contohnya: 10/0
maka ada exception ==> ZeroDivisionError
itu adalah exception dimana tidak boleh membagi
angka dengan angka 0

10 + 'qwe' ==> TypeError
exception utk tidak  memperbolehkan penambahan beda
type data.

abc ==> NameError
ini adalah exception dimana variavel tidak definisikan

x = (1,2)
x.asdasdas ===> AttributError
ini artinya exception tidak ada attribut yg yg bernama
'asdasdas'

utk melihat list Exception dari built-in function:

import builtins
help(builtins)

cara handling di python yaitu dgn

try:
...
except:
...

'''

result = None
a = float(input('number 1: '))
b = float(input('number 2: '))
# misal pembagian b = 0 maka ada error
# ini salah satu caranya handling jika terjadi
# exception maka akan diload bagian except:
try:
    result = a / b
except:
    print("float division by zero")

print('Result', result)

# utk yg lebih lengkap maka exception dngn cara
try:
    result = a / b
# Exception ini adalah BaseException pada builtins
# jika di buat type(e) maka ada <class 'ZeroDivisionError'>
except Exception as e:
    print("Error =",e)
    print("Error =",type(e))

print('Result', result)

# shingga lebih spesifik of exception
# exception lebih dr 1
try:
    result = a / b
except ZeroDivisionError as e:
    print("Error =",e)
except TypeError as e:
        print("Error =",type(e))

print('Result', result)

'''
lebih aman menggunakan Excepetion base sebagai
exception utk menggunakan nya supaya ketika inputnya
string bukan float maka semua bisa dihandle dengan base class
awal.

ada keyword else
digunakan utk mengeksekusi jika try bernilai true,
jika ada exception maka tidak akan di print di dlm
exception. Sedangkan finally baik saat benar atau tidak
saat try tetap dieksekusi data yg ada di bawah finally:

else: harus ada statement except:
tanpa except maka else statement tidak akan bisa dieksekusi
sdangkan finally: bisa dieksekusi tanpa ada nya error
'''

try:
    result = a / b
except ZeroDivisionError as e:
    print("Error =",e)
except TypeError as e:
        print("Error =",type(e))
else:
    print('__else__')
finally:
    print('__finally__')

print('Result', result)
