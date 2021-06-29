import Arithmetics
import unittest


class UnitTest_Arithmetics(unittest.TestCase):
    def run_test(self):
        arithmetics = Arithmetics.Arithmetics()
        # assert arithmetics.sum(2, 2) == 4
        self.assertAlmostEqual(arithmetics.sum(2, 2), 4)
        self.assertNotEqual(arithmetics.sub(6, 2), 2)
        self.assertEqual(arithmetics.sub(7, 2), 5)

        assert arithmetics.sub(5, 2) == 3
        assert arithmetics.mul(4, 2) == 8
        assert arithmetics.div(2, 2) == 1
        assert arithmetics.mod(3, 2) == 1
