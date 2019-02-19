'''
Unit testing
### wikipedia ###
unit testing is a software testing method by which individual
units of source code are tested to determine whether they are fit
for use.

Why unit test?
1. tests reduce bugs in new features and existing features
2. tests are good documentation
3. tests reduce the cost of change
4. faster debugging
4. faster development
5. better design

testing framework
1. unittest - in the python standard library
2. nose - not in the standard library. simpler tests than unittest
3. pytest - not in the python standard library



run :
    test biasa ==> pytest namafile.py
    test tiap fungsi ==> pytest namafile.py::test_namafungsi
    more detail ==> pytest namafile.py -v
    tiap fungsi sesuai nama yg di dlm kutip
    ==> pytest namafile.py -v -k "add" #run fungsi yg ada keyword add
    ==> pytest namafile.py -v -k "add or strings" #run fungsi yg ada keyword add atau strings
    ==> pytest namafile.py -v -k "add and strings"  #run fungsi yg ada keyword add dan strings

    -m utk marked expression, dmn fungsi test telah didekorasi(decoration)
    ==> pytest namafile.py -v -m strings # utk yg ada @pytest.mark.strings
    ==> pytest namafile.py -v -m number # utk yg ada @pytest.mark.number

    -x utk testing hingga ada kode yg failure dan di stop kemudian
    kode selanjutnya tdk akan di exekusi
    run : pytest namafile.py -v -x

    --tb=no utk mendisable detail failure
    run : pytest namafile.py -v -x --tb=no

    --maxfail=2 utk mengeksekusi 2 failure saja
    --maxfail=4 utk mengeksekusi 4 failure saja tegantung user brp inputan
    run : pytest namafile.py -v -maxfail=2

    jika jmlh failure sudah terpenuhi utk --maxfail=2 maka
    program akan distop dan ditunjukan detail fail

    jika ada decorasi :
@pytest.mark.skip(reason="do not run number add test")
maka fungsi ini tidak dieksekusi,
    run : 1. pytest namafile.py -v -rsx
          2. pytest namafile.py -v -r chars ==> utk lebih spesifik

@pytest.mark.skipif(sys.version_info < (3 ,7), reason="do not run number add test")
run : pytest namafile.py -v -r chars
    jika versi python < 3.7 maka fungsi di skip


    -s utk mengeksekusi print() di dlm testing CLI (command line interface)
    run: 1. pytest namafile.py -v -s
    run: 2. pytest namafile.py -v --capture=no


    -q utk quite information test artinya hanya menampilkan
    brp bnyak yg passed, failed
    run : 1. pytest namafile.py -v -q #detail OS,version, passed, failed
    run : 2. pytest namafile.py -q  #passed, failed

    atau jika ingin default utk 1 file:
    ==> py.test -v

ingat utk test maka tiap fungsi yg ditulis harus ada
prefix "test" seperti test_add() jika tidak ada atau
salah keyword maka tidak bisa passed atau tidak
dikenali (unrecognized),
bukan hanya nama fungsinya, file name nya juga harus ada
prefix "test"

jika namafile test ada prefix "test" maka bisa secara default
run test dengan py.test

jka nama file tidk ada prefix "test" maka harus
secara spesifik runningya yaitu: pytest namafile.py -v
'''

def add(x,y=2):
    return x+y

def product(x,y=2):
    return x*y
