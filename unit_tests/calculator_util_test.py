import unittest

from unit_tests import CalculatorUtil, InvalidException


class CalculatorUtilTest(unittest.TestCase):

    def test_addition(self):
        in1 = 10
        in2 = 20
        expected = in1 + in2
        calculatorUtil = CalculatorUtil(in1, in2)
        actual = calculatorUtil.addition()
        self.assertEqual(expected, actual)

    def test_subtraction(self):
        in1 = 10
        in2 = 20
        expected = in1 - in2
        calculatorUtil = CalculatorUtil(in1, in2)
        actual = calculatorUtil.subtraction()
        self.assertEqual(expected, actual)

    def test_multiplication(self):
        in1 = 30
        in2 = 10
        expected = in1 * in2
        calculatorUtil = CalculatorUtil(in1, in2)
        actual = calculatorUtil.multiplication()
        self.assertEqual(expected, actual)

    def test_division_float_success(self):
        in1 = 30
        in2 = 10
        expected = in1 / in2
        calculatorUtil = CalculatorUtil(in1, in2)
        actual = calculatorUtil.division_float()
        self.assertEqual(expected, actual)

    def test_division_float_fail(self):
        try:
            in1 = 30
            in2 = 0
            calculatorUtil = CalculatorUtil(in1, in2)
            calculatorUtil.division_float()
            self.fail("Expected Invalid Exception")
        except InvalidException as e:
            self.assertEqual(e.message, "B cannot be zero")


if __name__ == '__main__':
    unittest.main()
