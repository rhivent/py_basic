# break and continue
''' break keyword digunakan utk
menghentikan proses perulangan dan keluar dari perulangan

sedngkan continue digunakan utk melanjutkan program
perulangan dngn menskip data dari kondisi yg sudah
di deklarasikan dri if
'''
a = [0,1,2,3,4,5]
for x in a:
    if x == 3:
        break
    print(x) #hasil 0 1 2
print('##################')
# i = 0
# while i<5:
#     if i == 3:
#         continue
#     print(i)
#     i += 1
     # hasilnya 0 1 2 angka 3 di skip
    # akan tetapi stlh nilai 3 maka tidak diulang lgi
    # tetapi karena i += 1 ada di bawah print maka
    # ketika i =2 dan ditambah 1 shg nilainya 3 maka
    # terjadi infinite loop dmn i selalu 3 dan tidak di eksekusi
    # solusinya yaitu dengn menaruh i += 1 di atas kondisi if


i = 0
while i<5:
    if i == 5:
        print('finished')
    if i ==0:
        print(i)
    i += 1
    if i == 3:
        continue
    print(i)

    # hasilnya 0 1 2 4
