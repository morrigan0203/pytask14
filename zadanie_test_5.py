import unittest
import zadanie_5 as z5

class TestRectangle(unittest.TestCase):

    def test_summ(self):
        r = z5.Rectangle(20,30)
        r2 = z5.Rectangle(10)
        rs = r + r2
        self.assertEqual(rs.length, 10)
        self.assertEqual(rs.width, 60)

    def test_sub(self):
        r = z5.Rectangle(20,30)
        r2 = z5.Rectangle(10)
        rm = r - r2
        self.assertEqual(rm.length, 10)
        self.assertEqual(rm.width, 20)
    
    def test_eq(self):
        r = z5.Rectangle(20,30)
        r600 = z5.Rectangle(15, 40)
        self.assertTrue(r == r600)


if __name__=="__main__":
    unittest.main()

