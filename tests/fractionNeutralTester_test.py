from app.domain.fraction import Fraction
from app.services.fractionNeutralTester import FractionNeutralTester

def test_Fraction_Numerator_0_should_be_neutral():
  neutral = Fraction(0)

  isNeutral = FractionNeutralTester.IsNeutral(neutral)

  assert isNeutral == True

def test_Fraction_Numerator_1_should_not_be_neutral():
  neutral = Fraction(1)

  isNeutral = FractionNeutralTester.IsNeutral(neutral)

  assert isNeutral == False

def test_Fraction_Numerator_0_Denominator_2_should_be_neutral():
  neutral = Fraction(0,2)

  isNeutral = FractionNeutralTester.IsNeutral(neutral)

  assert isNeutral == True