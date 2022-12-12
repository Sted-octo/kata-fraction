from app.services.fractionAdditionCalculator import FractionAdditionCalculator
from app.domain.fraction import Fraction

def test_Add_neutral_fraction_to_any_fraction_should_return_base_fraction():
  base = Fraction(2,5)
  neutral = Fraction(0)

  sum:Fraction = FractionAdditionCalculator.Add(base, neutral)

  assert sum.numerator == base.numerator
  assert sum.denominator == base.denominator

def test_Add_any_fraction_to_neutral_fraction_should_return_toAdd_fraction():
  base = Fraction(0)
  anyFraction = Fraction(2,5)

  sum:Fraction = FractionAdditionCalculator.Add(base, anyFraction)
  
  assert sum.numerator == anyFraction.numerator
  assert sum.denominator == anyFraction.denominator