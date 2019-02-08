'''
if __name__ == "__main__":

digunakan utk menggantikan __name__ menjadi nama modul yg diimport
dan ada kondsi if __name__ == "__main__":
hal ini berguna ketika kita import tidak ingin mengakses code
selain dari yg dipanggil dari import

jika kita run kode file ini maka
akan diganti __name__ menajdi nama file yg diimport
sedangkan
jika kita run file mymath.py maka tampil
__main__
26
'''

import mymath

print(mymath.add(7,6))
# maka ter print
# mymath ==> __name__ diganti dengan amafile import sendiri
# 13
