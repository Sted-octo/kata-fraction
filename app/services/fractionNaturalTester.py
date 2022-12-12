from app.domain.fraction import Fraction

class FractionNaturalTester:
  def IsNatural(fraction:Fraction) -> bool:
    return fraction.denominator == 1