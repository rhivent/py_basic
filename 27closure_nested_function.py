'''
nested function is fungsi di dlm fungsi, contohnya:
def outer_function():
    def inner_function():
        print(text)
    inner_function()

outer_function("halo")

closure
cara mengkonversi nested function ke closure yaitu dengan me-return
inner_function() tanpa tanda ()

jadi, return inner_function

closure is a function whose return value depends on value of one or more
variable without declare outside the function,
contohnya:
def outer_function(text):
    def inner_function():
        print(text)
    return inner_function

a = outer_function("halo")
a() # hasilnya : halo

text ini adalah variable yg di declare diluar inner_function dan value of this
inner function depends on this text variable which is declare outside this inner_function
and that make is the closure. Close punya spesial property that the closure function objek
remember the value in the enclosing scope even if they are not present in the memory.

jadi closure adlh function objek yg mengingat nilai di enclosing scope even if they are not
present in the memory.

walaupun sudah didelete outer_function, tetap kita bisa mengakses di kedlm
inner_function yg sudah di deklarasikan ke dalm variabel a

closure digunakan supaya code lebih efesien dan faster di dlm
running
'''
# outer_function() is enclosing function
def outer_function(text):
    # declare locally in function
    # inner_function() is local function of this outer_function() fungsi
    def inner_function():
        print(text)
    # inisiate inner_function()
    inner_function()

outer_function("halo")  # tampil halo
print('########################')

def pop(list):
    def get_last_item(my_list):  # this is local function to pop()
        # mengembalikan nilai akhir yg di dapat contoh: my_list[4] = 5
        return my_list[len(list) - 1]

    # remove last item in the list, angka 5 terhapus
    list.remove(get_last_item(list))
    # mengembalikan semua elemen kedlm list
    return list

a = [1,2,3,4,5]
print(pop(a)) # hasilnya : [1, 2, 3, 4]
print(pop(a)) # hasilnya : [1, 2, 3]
print(pop(a)) # hasilnya : [1, 2]
print('########################')

# closure
def outer_function(text):
    def inner_function():
        print(text)
    return inner_function

a = outer_function("halo")
# a ini adalah inner_function karena
# sudah di declare bhw outer_function hanya me-return inner_function
del outer_function
# outer_function("halo") #mengecek keberadaan outer_function
a()  # hasilnya : halo



# closer contoh lainnya
def nth_power(exponent):
    def pow_of(base):
        return pow(base,exponent)
    return pow_of

# passing argumen exponent for outer fungsi
square = nth_power(2)
# passing argumen base for inner fungsi
print(square(2)) # hasilnya : 4
print(square(3)) # hasilnya : 9
print(square(4)) # hasilnya : 16
print(square(5)) # hasilnya : 25
