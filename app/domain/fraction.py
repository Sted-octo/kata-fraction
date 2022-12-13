class Fraction:
  def __init__(self, numerator:int=0, denominator:int=1):
    if denominator == 0:
      raise TypeError("denominator can't be equal to 0")
    self._numerator:int = numerator
    self._denominator:int = denominator

  @property
  def numerator(self):
    return self._numerator

  @property
  def denominator(self):
    return self._denominator