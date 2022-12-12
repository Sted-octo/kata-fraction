class Fraction:
    def __init__(self, numerator:int, denominator:int=1):
      if denominator == 0:
        raise TypeError("denominator can't be equal to 0")
      self.numerator = numerator
      self.denominator = denominator