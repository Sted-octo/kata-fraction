from app.domain.fraction import Fraction

class FractionAdditionCalculator:
  def Add(fractionBase:Fraction, fractionToAdd:Fraction) -> Fraction:
    if fractionToAdd.numerator == 0 and fractionToAdd.denominator == 1:
      return fractionBase
    if fractionBase.numerator == 0 and fractionBase.denominator == 1:
      return fractionToAdd
    return Fraction()