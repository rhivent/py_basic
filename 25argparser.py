'''
memparsing command line argumen ke script python,
butuh import argparse modul

ketika memakai parse_args() maka
semua argumen yg ada akan disimpan di dlm variabel
args.

ketika running program di command line (cli atau termux)
kita bisa memberikan  special argumen seperti -h utk help

contohnya: ke command line ,
tulis python3 nama_file (dlm hal ini nama file 25argparser.py) argumen( contohnya passing -h)

maka muncul:
usage: 25argparser.py [-h]

optional arguments:
  -h, --help  show this help message and exit

argparse.ArgumentParser() didlm kurung kita bisa mempassing beberapa argumen,
sesuai keinginan misal description,dll.

usage: 25argparser.py [-h]

my math script    =====>>> ini description

optional arguments:
  -h, --help  show this help message and exit

-h itu adalah parameter. Parameter ada 2 jenis yg bisa digunakan
pertama positional yg kedua optional
1. positional
contoh dibawah ini operator tambah

ketika di ketik di CLI atau termux python3 25argparser.py 8 20 +
maka isi dari varibel args :
Namespace(num1=8.0, num2=20.0, operator='+')

ketika di ketik di CLI atau termux python3 25argparser.py -h
isinya:
usage: 25argparser.py [-h] num1 num2 operator

my math script

positional arguments:
  num1        Number 1
  num2        Number 2
  operator    berikan operator

optional arguments:
  -h, --help  show this help message and exit

diatas ada penjelasan positional argument

jika menggunakan optional parameter maka tiap argument
diberikan --nama_argumen1
ketika di ketik di CLI atau termux python3 25argparser.py 8 20
walau sudah ada default pada argumen ketiga maka tidak akan jalan atau error

hal ini maka butuh python3 25argparser.py --num1 8 --num2 20
maka hasilnya 28 secara default akan melakukan operasi adding

python3 25argparser.py --num1 8 --num2 20 --operator -
hasilnya adalah -12 sesuai dengan kondisi operator.

python3 25argparser.py --operator / --num1 8 --num2 20
walau posisi tidak teratur tidak masalah selama nama optional parameter
benar maka positional tidak akan berubah sesuai nilai.

optional parameter bisa dibuat dengan shortform yaitu 1 huruf dengan
didepannya ada tanda 1 minus (-)
parser.add_argument('-n','--num1',help="Number 1",type=float)
-n disini adalah short parameter seperti -h alias dari --help

jika dirun python3 25argparser.py -h maka akan muncul:
usage: 25argparser.py [-h] [-n NUM1] [-i NUM2] [-o OPERATOR]
                      num1 num2 operator

my math script

positional arguments:
  num1                  Number 1
  num2                  Number 2
  operator              berikan operator

optional arguments:
  -h, --help            show this help message and exit
  -n NUM1, --num1 NUM1  Number 1
  -i NUM2, --num2 NUM2  Number 2
  -o OPERATOR, --operator OPERATOR
                        berikan operator

sehingga jika menggunakan -- maka eksekusi, ada spasi tiap inputan value:
python3 25argparser.py --operator / --num1 8 --num2 20

sehingga jika menggunakan - maka eksekusi, ada tanda = tiap inputan value:
python3 25argparser.py -o=/ -n=8 -i=20
hasilnya:
Namespace(num1=8.0, num2=20.0, operator='/')
0.4

jadi ini adalah shorthand notation
'''
import argparse

if __name__ == '__main__':
    # initial parser varibel
    parser = argparse.ArgumentParser(
        description = "my math script"
    )

    # add the parameter positional/optional
    # positional parameter
    # help disini semacam deskripsi utk user utk memberikan masukan seperti apa
    parser.add_argument('num1',help="Number 1",type=float)
    # secara default type yaitu string jika mau diganti tinggal tulis sesuai keinginan
    parser.add_argument('num2',help="Number 2",type=float)
    parser.add_argument('operator',help="berikan operator")

    # optional argument
    parser.add_argument('-n','--num1',help="Number 1",type=float)
    parser.add_argument('-i','--num2',help="Number 2",type=float)
    parser.add_argument('-o','--operator',help="berikan operator", default='+')

    # parse the arguments
    args = parser.parse_args()
    print(args)
    result = None
    # providing mathematical operation
    # add
    if args.operator == '+':
        # mengembalikan nilai ke variabel result
        result = args.num1 + args.num2
    # minus
    if args.operator == '-':
        # mengembalikan nilai ke variabel result
        result = args.num1 - args.num2
    # devide
    if args.operator == '/':
        # mengembalikan nilai ke variabel result
        result = args.num1 / args.num2
    # multiplication
    if args.operator == '*':
        # mengembalikan nilai ke variabel result
        result = args.num1 * args.num2
    # pangkat /power
    if args.operator == 'pow':
        # mengembalikan nilai ke variabel result
        # power itu dengn ** atau pangkat
        result = pow(args.num1,args.num2)

    print(result)
