'''
decorators wrap a function and modify its behaviour
in one way or the another without having to directly change the
source code of the function being decorated

# bisa di deklarasikan lebih simple utk pendekorasian fungsi
caranya dengan menulis kode @nama_fungsi_dekorator tepat diatas
fungsi yg ingin didekorasikan

'''

# membuat fungsi decorator
def decorator_function(func):
# mempassing fungsi sebagai argumen
    def wrapper_function():
        print("X" * 20)
        # isinya memanggil funcgi yg dipassing sbg argumen
        func()
        print("Y" * 20)
    return wrapper_function #tanpa () sebagai closure
# ini adalh simple form of decorator fungsi

@decorator_function
def say_halo():
    print("halo")

# cara memanggil fungsinya decorators dngn menampung di variabel dulu
# kemudian di panggil sebgi inner fungsi, tanpa @decorator_function
# halo_var = decorator_function(say_halo)  # bisa di deklarasikan lebih simple
# halo_var() # memanggil wrapper_function

say_halo() # dengan @decorator_function, hasilnya sama

'''
hasilnya :
XXXXXXXXXXXXXXXXXXXX
halo
YYYYYYYYYYYYYYYYYYYY
'''
print("###########################################")
# try another example, dekorasi lebih dari 2 utk 1 fungsi
def decorator_A(func):
    def wrapper_A():
        print("X" * 20)
        func()
        print("X" * 20)
    return wrapper_A
def decorator_B(func):
    def wrapper_B():
        print("Y" * 20)
        func()
        print("Y" * 20)
    return wrapper_B
@decorator_B
@decorator_A
def halo():
    print("halo halo")

# 1. cara convensional
# display_halo = decorator_B(decorator_A(halo))  # cara menampung kedlm variabel jika lebih dari 1 decorator fungsi
# display_halo()
# 2. cara cepat
halo()

'''
hasilnya :
YYYYYYYYYYYYYYYYYYYY
XXXXXXXXXXXXXXXXXXXX
halo halo
XXXXXXXXXXXXXXXXXXXX
YYYYYYYYYYYYYYYYYYYY
'''

print("###########################################")

# contoh lainnya
def decorator_C(func):
    def wrapper_C(a,b):  # menapung 2 nilai dr paramter yg dipassing dr fungsi yg dipanggil
        print('pembagian antara:',a,'and',b)
        if b == 0:
            print('penyebut 0 tidak bisa diizinkan')
            return 'silahkan ganti penyebut'
        return a/b
        func()
        print('Y' * 20)
    return wrapper_C

# calling decorator fungsi diatas fungsi normal kita
@decorator_C
def divide(x,y):
    return x/y

print(divide(10,0))


# contoh lainnya
print("###########################################")
# disini kita ingin membuat generic decorator
# dimana waktu kita panggil tidak tergantung pada satu fungsi saja
# dan argumen bisa bebas inputnya, bisa 2, 3, 5,atau tidak ada argumen
# disini kita ingin menghitung brp lama waktu yg dibutuhkan
# utk eksekusi fungsi normal sblm didekorasikan,
# buat fungsi timing decorator tuk measure fungsi normal, import modul time

from time import time # ada built-in function utk measure time
def timing(func):
    def wrapper_func(*args,**kwargs): #flexsibel wrapper tidak tergantung dr brp bnyak argumen yg di input
        start_time = time() # menyimpan waktu skrng,
        print(start_time)
        result = func(*args,**kwargs) #menyimpan hasil dari eksekusi fungsi, dngn flexibel parameter
        end_time = time()
        print(end_time)

        print('Elapsed time: {}'.format(end_time - start_time)) # memnunjukan jangka waktu eksekusi
        return result
    return wrapper_func
# calling decorator fungsi diatas fungsi normal kita
@timing
def total_sum(num):
    sum = 0
    for z in range(num+1):
        sum += z

    return sum

# calling totaling
print(total_sum(20000000))  # hasilnya time semakin lama jika nilai lebih banyak
