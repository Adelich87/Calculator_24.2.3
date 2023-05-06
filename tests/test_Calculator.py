import pytest

from app.calc import Calculator


class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_subtraction_good(self):
        assert self.calc.subtraction(self, 11, 2) == 9

    def test_adding_good(self):
        assert self.calc.adding(self, 18, 129) == 147

    def test_multiply_good(self):
        assert self.calc.multiply(self, 13, 7) == 91

    def test_division_good(self):
        assert self.calc.division(self, 18, 2) == 9.0

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print("Метод Teardown выполнен")






