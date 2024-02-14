from src.dev import math_operations


def test_add():
    result= math_operations.add(2, 3)
    assert result == 5

def test_sub():
    result= math_operations.sub(5, 3)
    assert result == 2

def test_divide():
    result= math_operations.divide(10, 2)
    assert result==5

def test_divide_by_zero():
    try:
        math_operations.divide(5, 0)
    except ZeroDivisionError as e:
        assert str(e) == "Cannot divide by Zero"

def test_getting_average():
    l=[1,2,3,4,5]
    result= math_operations.average(l)
    assert result==3

def test_avg_with_empty_list():
    l=[]
    result = math_operations.average(l)
    assert result == 0

def test_operations():
    result= math_operations.operation(10, 2)
    assert result==(5,20,12,8)

def test_operation_with_zero():
    try:
        math_operations.operation(10, 0)
    except ZeroDivisionError as e:
        assert str(e)=="Cannot divide by Zero"



