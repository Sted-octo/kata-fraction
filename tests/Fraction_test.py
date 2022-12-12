from app.domain.fraction import Fraction
import pytest


def test_fraction_without_denominator_should_init_denominator_equal_to_1():
  noDenominator:Fraction = Fraction(0)
  assert noDenominator.denominator == 1

def test_fraction_denominator_2_should_init_denominator_equal_to_2():
  withDenominator:Fraction = Fraction(0,2)
  assert withDenominator.denominator == 2

def test_fraction_denominator_0_should_raise_typeError_exception():
  with pytest.raises(TypeError):
    Fraction(0,0)

def test_fraction_without_arguments_should_init_numerator_to_0_and_denominator_equal_to_1():
  noArgs:Fraction = Fraction()
  assert noArgs.numerator == 0
  assert noArgs.denominator == 1

def test_fraction_numerator_2_should_init_numerator_equal_to_2():
  onlyNumerator:Fraction = Fraction(2)
  assert onlyNumerator.numerator == 2