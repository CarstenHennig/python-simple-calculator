from calculator import Calculator


assert =

class TestCalculator(pytest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        with self.assertRaises(ValueError):
            self.calc.divide(4, 0)

    def test_nth_root(self):
        self.assertAlmostEqual(self.calc.nth_root(8, 3), 2.0)
        with self.assertRaises(ValueError):
            self.calc.nth_root(-8, 3)

    def test_memory(self):
        self.calc.memory_store(5)
        self.assertEqual(self.calc.memory_recall(), 5)
        self.calc.memory_store(-3)
        self.assertEqual(self.calc.memory_recall(), -3)

if __name__ == '__main__':
    unittest.main()



'''import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        with self.assertRaises(ValueError):
            self.calc.divide(4, 0)

    def test_nth_root(self):
        self.assertAlmostEqual(self.calc.nth_root(8, 3), 2.0)
        with self.assertRaises(ValueError):
            self.calc.nth_root(-8, 3)

    def test_memory(self):
        self.calc.memory_store(5)
        self.assertEqual(self.calc.memory_recall(), 5)
        self.calc.memory_store(-3)
        self.assertEqual(self.calc.memory_recall(), -3)'''


'''from Calculator import calculator



class MyTestCase(unittest.TestCase):

'''
    def setUp(self, memory: float = 100) -> None:
        self.calculator = calculator()
        self.memory = calculator(memory)
'''

    def test_addition(self) -> None:
        self.assertEqual(self.memory.addition(10, 30), 40.0)

    def test_subtraction(self) -> None:
        self.assertEqual(self.memory.subtraction(100, 30), 70)

    def test_multiplication(self) -> None:
        self.assertEqual(self.memory.multiply(10, 10), 100)

    def test_division(self) -> None:
        self.assertEqual(self.memory.division(35, 7), 5)

    def test_memory(self) -> None:
        self.assertEqual(self.memory.memory, 100.0)

    def test_memory_reset(self) -> None:
        self.assertEqual(self.memory.reset_memory(), None)


if __name__ == '__main__':
    unittest.main()'''
