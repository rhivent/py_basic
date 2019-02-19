import math_func2
import pytest
import sys
# sys.version_info < (3 ,7) ==> 3 adalah major version , 7 adlh minor version
# @pytest.mark.skip(reason="do not run number add test")
@pytest.mark.skipif(sys.version_info < (3,5), reason="do not run number add test")
def test_add():
    assert math_func2.add(7,3) == 10
    assert math_func2.add(7) == 9

@pytest.mark.number
def test_product():
    assert math_func2.product(5,5) == 24
    assert math_func2.product(5) == 10
    print(math_func2.product(5,5),'+++++++++++++++')

@pytest.mark.strings
def test_add_strings():
    result = math_func2.add("Hello"," World")
    assert result == "Hello World"
    assert type(result) is str
    assert "HMLA" not in result

@pytest.mark.strings
def test_product_strings():
    assert math_func2.product("hello ",3) == "hello hello hello "
    result = math_func2.product("hello ")
    assert result == "hello hello "
    assert type(result) is str
    assert "hello" in result
