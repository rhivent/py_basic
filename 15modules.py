'''
module is the python file,
caranya mengakses dngn keyword import

cara membuat module sendiri yaitu:
disini kita membuat file baru 15myfunction.py

jika beda folder modulnya maka aksesnya dngn
from directory import namafile

utk import file yg ada class maka syntax
from namafile import namaclass
'''
import math
# jika dalam satu folder maka tinggal import namafile
# import myfunction

from module import myfunction
print(myfunction.multiply(5,7))
print(myfunction.add(5,7))

# atau dengn cara
import module.myfunction
print(module.myfunction.multiply(5,7))
print(module.myfunction.add(5,7))

# atau dngn cara merename supaya tidak kepjngnan
import module.myfunction as mf
print(mf.multiply(5,7))
print(mf.add(5,7))

# atau caranya dengan
from module import myfunction as mf
print(mf.multiply(5,7))
print(mf.add(5,7))

# contoh lain ada di folder module
