import Test_Arithmetics
import UnitTest_Arithmetics


def sum(a, b):
    return a + b


def test_case():
    # assert (2 + 2) == 4
    assert sum(2, 2) == 4


def test_hello(name):
    assert name == 'Hello'


if __name__ == '__main__':
    test_case()
    test_hello('Hello')
    Test_Arithmetics.Test_Arithmetics().run_test()
    UnitTest_Arithmetics.UnitTest_Arithmetics().run_test()
