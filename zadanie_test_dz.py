import unittest
import zadanie_dz as dz

class TestFactorial(unittest.TestCase):

    def setUp(self) -> None:
        self.f = dz.Factorial(70, 10)

    def test_factorial_3(self):
        self.assertEqual(self.f(3), 6)
    
    def test_factorial_5(self):
        self.assertEqual(self.f(5), 120)



if __name__=="__main__":
    unittest.main()