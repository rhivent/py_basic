'''
variabel lokal and global

variabel lokal biasanya ada di dlm fungsi
sedngkan yg global ada di luar class atau fungsi

ketika kita memakai keyword global var maka, nilai
variabel yg diluar ditangkap kedlm fungsi
dan jika di fungsi ada nama variabel yg sama dngn nama
variabel global maka, nilai variabel global akan di
timpa (reassign/overwritten) shg berubah datanya

print('3--------',x) # local

nonlocal varibel mirip dngn global varibel, tpi
berada di nested fungsi.


ketika hasil contoh dibawah 50,100,20 dmn setiap
x = 50 dr print(x) sblm inner() dipanggil
x = 100 dr print(x) stlh inner() dipanggil dan overwritten x secara locally didlm fungsi
x = 20 dr global scope, dmn jika di dlm fungsi tdk ada keyword global maka
otomatis tidak akan tertimpa dr nilai yg berubah di fungsi func2() saat dipanggil
'''
def func():
    x = "local"
    print(x) # local

x="global"
func()  # exekusi fungsi func()
print(x) # global

print('###################################')

def func1():
    global x
    print('1--------',x) # global
    x = "local"
    print('2--------',x) # local

x="global"
func1()  # exekusi fungsi func()
print('3--------',x) # local

print('###################################')
def func2():
    x=50
    def inner():
        nonlocal x
        x=100
    print('1--------',x) # 50
    inner()
    print('2--------',x) # 100

x=20
func2()  # exekusi fungsi func()
print('3--------',x) # 20

print('###################################')
def func3():
    x=50
    def inner():
        global x
        x=100
    print('1--------',x) # 50 local
    inner()
    print('2--------',x) # 50 local
# nilai 50 karena blm di ada globally dan diprint seblm inner() dipanggil
# nilai 50 kedua tidak efek dr keyword global, krn diabil secara locally x=50
# nilai x di overwritten krn ada global keyword x=100
x=20
func2()  # exekusi fungsi func()
print('3--------',x) # 100
