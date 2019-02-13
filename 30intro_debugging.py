'''
debugger : jadi ketika kita utk merun script kita di berbagai server, dan
tidak semua ada IDE, kebanyakan memakai CLI(terminal), ini gunanya debugger
memakai command line script.

simple debug dibawah menghasilkan angka penambahan yg tidak semestinya,
maksudnya ketika kita input 1 dan input 2 maka muncul hasil 12 bukan 3, jika
org yg sudah tau pasti dikarenakan typenya adalh string sedangkan jika tidak
maka ini yg harus di debug, supaya sistem berjalan sesuai dngn fungsi
yg diinginkan.

memakai library pdb.
running di terminal :
    python3 -m pdb nama_script_.py

ketik help ===> maka muncul list command,
ketik help next  ====> tampil deskripsi penggunaan command,
disini bisa debug sesuai command list yg ada.

ketik n maka akan ke next line pada 30debugging.py setelha fungsi def ...,
ketik where akan tampil dmn letak pdb status saat ini,

ketik continue maka akan melanjutkan program yg dirunning, dari letak terakhir
pdb status itu berada.

setelah program selesai diexekusi, otomatis pdb restarting ke awal top line.

sebenarnya kita ingin program ini penambahan angka numerik, akan tetapi di
program ini hasilnya penggabungan 2 angka menjadi 1,

ketik whatis x setelah execusi input data x, hasilnya <class 'str'> artinya
x bertipe string bukan integer, dari sini kita tau persamasalhannya.

tanda + itu concate dari 2 string yg ingin digabung, sedangkan fungsi input()
defaultnya adalah string, shg tidak menambah calculasi secara biasa.

skrng diubah bagian input menjadi int(input()) dan RESTARTED PDB
ketik break baris_ke_brp  ==> fungsinya mematikan program pd line tertentu

kemudian ketik continue dan akan eksekusi biasa input 1 , input 2,
kemudian whatis x maka sudah berubah jadi integer sesuai dngn tipe data
yg diinginkan.

ketik q utk exit dr pdb debugger.

jika ingin import debugger, ketik di kode import pdb
break point maka ketik pdb.set_trace()

ketika sudah import di kode maka running kode di CLI/terminal : python3 nama_script_.py
tanpa harus ada -m pdb krn sudah otomatis diload, ketika menulis pdb.set_trace()
maka akan otomatis stop di line yg sesuai set_trace().

terkadang org ingin melakukan debug pada line tertentu saja, contohnya

...
line 12
import pdb;pdb.set_trace()
line 14
...
ini dapat menguntungkan krn dr sini bisa tau jika hal ini bertujuan utk membuat
program bekerja semestinya, jika sudah work maka tinggal dihapus dalm 1 line
debug itu.

jika melakukan debug dari shell python maka:
ketik python3 ==> masuk ke shell
ketik import 30debugging ==> masukkan nama file atau direktori
ketik import pdb ==> import pdb library
ketik pdb.run(30debugging.nama_fungsinya())  ===> uncomment fungsi main dan
delete dari var x di if __name__ == ... kecuali main()
done...

ingat selalu restart pdb ketika merubah kode di dlm script.
retart dengan quit dan masuk ke pdb lgi. 
'''
# contoh simple debug
import pdb
def add(x,y):
    sum = x + y
    return sum

if __name__ == "__main__":
    x = int(input("Num 1 : "))
    y = int(input("Num 2 : "))
    pdb.set_trace()  # set break point
    # import pdb;pdb.set_trace()
    z = add(x,y)
    print(z)
# run in termux atau terminal/command line interface
