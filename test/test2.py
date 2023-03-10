import pytest


def oper(a, b):
    return a / b


def test_oper():
    assert oper(10, 5) == 2


# "==================2Вариант================"

# @pytest.mark.skip()
# def test_oper1():
#     assert oper(10, 5) == 2


# def test_oper2():
#     assert oper(20, 5) == 100


# def test_oper3():
#     assert oper(10, 2) == 6


# def test_oper4():
#     assert oper(0, 1) == 0


# "=====================3Вариант=================="

# # Отличный вариант


# @pytest.mark.parametrize(
#     "num1, num2, result",
#     [(10, 5, 2),
#      (20, 5, 4),
#      (10, 2, 5),
#      (0, 1, 0)]
# )
# def test_oper_5(num1, num2, result):
#     assert oper(num1, num2) == result


@pytest.mark.parametrize("a,b,error", [(10,"str", TypeError)(10,0,ZeroDivisionError)]

def test_oper_error(a,b,error):

