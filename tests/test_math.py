import pytest
from orders.math import inc, divide


def test_answer():
    print('test answer...')
    assert inc(3) == 4

# @pytest.skip
def test_divide_zero():
    with pytest.raises(ValueError):
        divide(1, 0)