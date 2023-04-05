import pytest
from series import fibonacci , lucas ,sum_series




def test_1():
    actual=fibonacci(0)
    expected=0
    assert actual == expected


def test_2():
    actual=fibonacci(1)
    expected=1
    assert actual == expected

def test_3():
    actual=fibonacci(2)
    expected=1
    assert actual == expected

def test_3():
    actual=fibonacci(3)
    expected=2
    assert actual == expected

def test_4():
    actual=lucas(0)
    expected=2
    assert actual == expected

def test_5():
    actual=lucas(2)
    expected=3
    assert actual == expected

def test_6():
    actual=lucas(4)
    expected=7
    assert actual == expected

def test_7():
    actual=sum_series(0)
    expected=0
    assert actual == expected

def test_8():
    actual=sum_series(3)
    expected=2
    assert actual == expected

def test_8():
    actual=sum_series(4,2,1)
    expected=7
    assert actual == expected