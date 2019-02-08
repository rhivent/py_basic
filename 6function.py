# a function is a group of statements within a program
# that together perform a specific task.
# function can have no argument

'''
    def functionname(arg1,arg2,...):
    statement1
    statement2
    ...
'''
# deklarasi function
def hello(name):
    print('halo',name)
# memanggil fungsi
hello("mark")

# deklarasi function
def add(x,y):
    if type(x) != type(y):
        print("Please give the args of same type")
        # jika return keyword tanpa ada apa2 maka kode dibawah fungsi tidak dieksekusi
        return
    return (x+y)
# memanggil fungsi
print('Total is',add(100,200))
print(add("halo",123))

# default value in argument for user not passing any parameter
def score(name="default name",score=0):
    print(name,"has score",score)
score()
# menimpa default value pada parameter name
score("mark")
# menimpa default value pada parameter score
score(score=12)
score("mark",30)

''' tanda * membuat kita dapat menginput
parameter untuk argumen score lebih dari 1
'''
def score(name="default name",*score):
    print(name,"has score :")
    for x in score:
        print(x)
# jika ingin pake len() utk
# mengetahui panjang data
# pd argumen disarankan argumen
# dngn tanda * diletakkan pada akhir argumen
score("ventus",60,70,80,90)
'''
akan ada value (60,70,80,90) ini dinamakan tuple
sama sperti list atau array tetapi kita hanya bisa read
tidak bisa di modifikasi atau delete dari element di list ini
'''

'''  bisa juga dngn tanda **arg
tanda ini bisa digunakan utk membuat
argumen dengn key=value pairs
utk tanda * maka didapat data type tuple
utk tanda ** maka didapat data type dictionary
'''
def student(name,age,**marks):
    print("name: ",name)
    print("age: ",age)
    # print("marks",marks)
    for key,value in marks.items():
        print(key,'=',value)
student('tom',22,english=90,math=100,physics=90,biology=90)
