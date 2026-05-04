from primo import is_primo
import pytest

@pytest.mark.parametrize("input, expected", [
    (2, True),
    (0, False),
    (1, False),
    (-2, False),
    (-7, False),
    (1987, True),
    (1986, False),
])
def test_primo(input, expected):
    assert is_primo(input) == expected

def test_primo_string_1987():
    assert is_primo("1987") == True

def test_primo_string_vazia():
    assert is_primo("") == False

def test_primo_string_O():
    assert is_primo("O") == False
