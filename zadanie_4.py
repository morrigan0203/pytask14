import pytest
import zadanie_1_2 as z

def test_without_changes():
    assert z.alfaStr("without changes") == 'without changes'

def test_without_changes_symbols():
    assert z.alfaStr("without CHANGES symbols") == 'without changes symbols'

def test_delete_points():
    assert z.alfaStr("delete. points...") == 'delete points'

def test_delete_non_english_symbols():
    assert z.alfaStr("delete non english символов") == 'delete non english '

def test_remove_all_non_english_symbols():
    assert z.alfaStr("remove. ALL: non английских english symbols") == 'remove all non  english symbols'


if __name__ == '__main__':
    pytest.main()
