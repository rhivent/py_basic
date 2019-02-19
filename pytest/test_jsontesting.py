from jsontesting import StudentDB
import pytest

'''
problem disini yaitu kita repeat koneksi ke DB, jika ada
data > 1000 dan kedua yg memori akan overload jk
di inisialiasi terus2 , dan konsumsi resource di sistem
akan sangat bnyak

solusinya yaitu membuat setup dan tear_down method
seperti fungsi __constructor() di PHP supaya dieksekusi
kode utk semua.

jadi kode setup_module() akan starting ketika pytest dan
pytest akan recognized every module

after test kita bisa menclose koneksi dengan teardown_module()


run : pytest namafile.py -v -s ===> utk eksekusi print()


fixture() ==> utk menstarting atau close the method
tanpa harus menggunakan setup_module(module) dan
teardown_module(module) dan hanya setup pada awal test,
test selanjutnya bisa diikuti sesuai setup awal.

ini adalah manfaat dari @pytest.fixture(scope="module")
'''
@pytest.fixture(scope="module")
def db(): #karna tiap fngsi ada db
    print('+++++++++++++setup+++++++++++++')
    db = StudentDB()
    db.connect('data.json')
    # return db
    yield db

    # utk close koneksi dengan teardown dan mengubah return db menjadi yield db
    print('++++++++++++++teardown+++++++++++++')
    db.close()

# db = None
# def setup_module(module):
#     global db
#     print('+++++++++++++++++++++++++++++++++setup+++++++++++++++++++++++++++++++++')
#     db = StudentDB()
#     db.connect('data.json')

# def teardown_module(module):
#     print('+++++++++++++++++++++++++++++++++teardown+++++++++++++++++++++++++++++++++')
#     db.close() # free resources system

def test_scott_data(db):
# def test_scott_data():
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_mark_data(db):
# def test_mark_data():
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'
