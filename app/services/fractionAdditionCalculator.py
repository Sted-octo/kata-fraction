from app.domain.fraction import Fraction
from app.services.fractionNeutralTester import FractionNeutralTester

class FractionAdditionCalculator:
  def Add(base:Fraction, toAdd:Fraction) -> Fraction:
    if FractionNeutralTester.IsNeutral(toAdd):
      return base
    if FractionNeutralTester.IsNeutral(base):
      return toAdd

    if base.denominator == toAdd.denominator:
      return Fraction(base.numerator + toAdd.numerator, base.denominator)

    return Fraction(base.numerator * toAdd.denominator + toAdd.numerator * base.denominator, base.denominator * toAdd.denominator)