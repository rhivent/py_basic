import func3
import pytest
# parameter utk memanggil testing tiap asserting dlm 1 fungsi
# parameter x and y utk dipassing ke fungsi , result parameter
# utk mempassing data yg ada maka butuh argumen terakhir dlm
# btk list [] dan didalamnya ada tuple ()
# argumen terakhir akan di iteratable
@pytest.mark.parametrize('x,y,result',
                        [
                            (7,3,10), # 7 = x, 3=y, 10 = result
                            ("hello"," dunia","hello dunia"),
                            (10.5,25.5,36)
                        ]

                    )
def test_add(x,y,result):
    assert func3.add(x,y) == result
    # result = func3.add("hello"," dunia")
    # assert result == "hello dunia"
    # result = func3.add(10.5,25.5)
    # assert result == 36

'''
ketika memakai parametrize(), maka tidak perlu memanggil
1 persatu berkali2 di testing.
yang dibutuhkan adalah memberikan parameter pada
fungsi yg ingin di test dan juga pada
asserting data yg ingin dirun

shg hanya butuh:
===> assert func3.add(x,y) == result

ingat 'x,y,result' tidak dipisah 'x','y','result'
tetapi 1 string didlmnya dipisah dengan tanda ,



run : pytest test_func3.py -v
'''
