from hypothesis_poc import divrem

from hypothesis import given
from hypothesis.strategies import integers

@given(numerator=integers(), divisor=integers())
def test_hypothesis_poc_divrem(numerator, divisor):
    (quotient, remainder) = divrem.divrem(numerator, divisor)
    assert type(quotient) == int
    assert type(remainder) == int
