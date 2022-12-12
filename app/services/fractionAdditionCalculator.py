from app.domain.fraction import Fraction
from app.services.fractionNeutralTester import FractionNeutralTester

class FractionAdditionCalculator:
  def Add(fractionBase:Fraction, fractionToAdd:Fraction) -> Fraction:
    if FractionNeutralTester.IsNeutral(fractionToAdd):
      return fractionBase
    if FractionNeutralTester.IsNeutral(fractionBase):
      return fractionToAdd
    return Fraction()