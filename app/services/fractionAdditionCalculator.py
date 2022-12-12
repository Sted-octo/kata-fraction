from app.domain.fraction import Fraction
from app.services.fractionNeutralTester import FractionNeutralTester
from app.services.fractionNaturalTester import FractionNaturalTester

class FractionAdditionCalculator:
  def Add(base:Fraction, toAdd:Fraction) -> Fraction:
    if FractionNeutralTester.IsNeutral(toAdd):
      return base
    if FractionNeutralTester.IsNeutral(base):
      return toAdd

    if FractionNaturalTester.IsNatural(base) and FractionNaturalTester.IsNatural(toAdd):
      return Fraction(base.numerator + toAdd.numerator)

    if base.denominator == toAdd.denominator:
      return Fraction(base.numerator + toAdd.numerator, base.denominator)

    return Fraction()