import Arithmetics
import unittest


class Test_Arithmetics:
    def run_test(self):
        arithmetics = Arithmetics.Arithmetics()
        assert arithmetics.sum(2, 2) == 4
        assert arithmetics.sub(5, 2) == 3
        assert arithmetics.mul(4, 2) == 8
        assert arithmetics.div(2, 2) == 1
        assert arithmetics.mod(3, 2) == 1