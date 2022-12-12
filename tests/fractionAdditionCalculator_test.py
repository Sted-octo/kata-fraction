from app.services.fractionAdditionCalculator import FractionAdditionCalculator
from app.domain.fraction import Fraction

def test_add_neutral_fraction_to_any_fraction_should_return_base_fraction():
  base = Fraction(2,5)
  neutral = Fraction(0)

  sum:Fraction = FractionAdditionCalculator.Add(base, neutral)

  assert sum.numerator == base.numerator
  assert sum.denominator == base.denominator

def test_add_any_fraction_to_neutral_fraction_should_return_to_add_fraction():
  base = Fraction(0)
  anyFraction = Fraction(2,5)

  sum:Fraction = FractionAdditionCalculator.Add(base, anyFraction)

  assert sum.numerator == anyFraction.numerator
  assert sum.denominator == anyFraction.denominator

def test_two_natural_fractions_should_return_natural_fraction_with_sum_of_numerators():
  base = Fraction(5)
  anyFraction = Fraction(2)

  sum:Fraction = FractionAdditionCalculator.Add(base, anyFraction)

  assert sum.numerator == 7
  assert sum.denominator == 1

def test_identical_denominators_should_return_numerators_sum_and_same_denominator():
  denominator = 7
  base = Fraction(5,denominator)
  toAdd = Fraction(3,denominator)

  sum:Fraction = FractionAdditionCalculator.Add(base, toAdd)

  assert sum.numerator == 8
  assert sum.denominator == denominator
