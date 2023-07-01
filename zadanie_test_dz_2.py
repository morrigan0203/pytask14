import pytest
import zadanie_dz as dz

@pytest.fixture
def fact():
    return dz.Factorial(70,10)

def test_factorial_3(fact):
    assert fact(3) == 6

def test_factorial_5(fact):
    assert fact(5) == 120


if __name__=="__main__":
    pytest.main(['-v'])
