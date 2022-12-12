from app.domain.fraction import Fraction
from app.services.fractionNeutralTester import FractionNeutralTester
from app.services.fractionNaturalTester import FractionNaturalTester

class FractionAdditionCalculator:
  def Add(fractionBase:Fraction, fractionToAdd:Fraction) -> Fraction:
    if FractionNeutralTester.IsNeutral(fractionToAdd):
      return fractionBase
    if FractionNeutralTester.IsNeutral(fractionBase):
      return fractionToAdd

    if FractionNaturalTester.IsNatural(fractionBase) and FractionNaturalTester.IsNatural(fractionToAdd):
      return Fraction(fractionBase.numerator + fractionToAdd.numerator)

    return Fraction()