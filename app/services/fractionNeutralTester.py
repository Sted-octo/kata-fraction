from app.domain.fraction import Fraction

class FractionNeutralTester:
  def IsNeutral(fraction:Fraction) -> bool :
    return fraction.numerator == 0