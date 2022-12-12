from app.domain.fraction import Fraction
from app.services.fractionNaturalTester import FractionNaturalTester

def test_fraction_denominator_1_should_be_natural():
  natural = Fraction(1,1)

  isNatural = FractionNaturalTester.IsNatural(natural)

  assert isNatural == True


def test_fraction_denominator_2_should_not_be_natural():
  natural = Fraction(1,2)

  isNatural = FractionNaturalTester.IsNatural(natural)

  assert isNatural == False

def test_neutral_fraction_should_be_natural():
  natural = Fraction()

  isNatural = FractionNaturalTester.IsNatural(natural)

  assert isNatural == True