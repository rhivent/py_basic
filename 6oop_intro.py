'''
procedural programming
ciri:
1. bhs C, pascal dll
2. basic unit utama adlah fungsi
3. concentrates on creating functions shg kekurangannya 4.
4. data dan operations on the data are separated mka butuh 5.
5. methodology requires sending data to procedure/functions

contoh:
#travel

Global Data
travel {
    openApp()
    bookCap()
    waitForTheCab()
    sitInTheCab()
    reachDestination()
    PayCabFare()
}

yg dilakukan procedural programming yaitu create some
Global Data (data struktur utk menampung semua data),
stlh di store data, maka design alogarithm, shg consentrasi
membuat fungsi, data dan operations on data terpisah dan butuh
method utk mendapat/mengirim data ke fungsi.
Artinya setelah fungsi dieksekusi hanya result data
tidak bisa menyimpan/hold state of data, jika ingin
menggunakan data some other place in code shg sangat susah,
using this kind of function (procedural programming).

##################
Konsep OOP
ciri :
1. bhs C++,Java, Python
2. basic unit adalh class
3. centered on creating objects
4. Object: a single software unit that combines data
and methods
5. Data in an object are known as attributes.
6. Procedures/functions in an object are known as methods.

pengertian class : referensi dari blueprint yg punya data dan methods
method adalah fungsi yg ada di dlm class
attribute adalah data di dlm object class atau variabel
                yg bisa menampung data-data
sehingga class ini bisa dibuat object, artinya bisa membuat
beda object dengan berbeda class.
Object = combinasi antara data dan method
sehingga antar class bisa bertukar data dari object
yg telah diinisiasi shg data bisa disimpan di dlm object
misal data passenger bisa mengakses data dari class Cab

contoh:
class Cab{
    cabService, merkCab,location, numberPlate # data
    cabService berisi Uber,Gojek,dll
    merkCab isinya toyota,honda,dll
    location isinya data geolocation
    numberPlate isinya plat nomor kendaraan
    book(),arrival(),start() # methods
}

class CabDriver {
    name,employeeId # data
    openDoor(), drive() #methods
}

class passenger {
    name,address # data
    openApp(),bookCab(),walk() #methods
}

jadi data dan method di procedural programming itu
terpisah, sdangkan di dlm OOP data dan method ada di dlm objek
'''
