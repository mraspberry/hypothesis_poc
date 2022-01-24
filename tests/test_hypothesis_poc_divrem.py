from hypothesis_poc import divrem

from hypothesis import given
from hypothesis.strategies import integers

@given(numerator=integers(), divisor=integers())
def test_hypothesis_poc_divrem(numerator, divisor):
    assert divrem.divrem(numerator, divisor)
