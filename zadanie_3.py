import unittest
import zadanie_1_2 as z

class TestAlfaStr(unittest.TestCase):

    def test_without_changes(self):
        self.assertEqual(z.alfaStr("without changes"), 'without changes')

    def test_without_changes_symbols(self):
        self.assertEqual(z.alfaStr("without CHANGES symbols"), 'without changes symbols')

    def test_delete_points(self):
        self.assertEqual(z.alfaStr("delete. points..."), 'delete points')

    def test_delete_non_english_symbols(self):
        self.assertEqual(z.alfaStr("delete non english символов"), 'delete non english ')

    def test_remove_all_non_english_symbols(self):
        self.assertEqual(z.alfaStr("remove. ALL: non английских english symbols"), 'remove all non  english symbols')


if __name__=="__main__":
    unittest.main()
    
