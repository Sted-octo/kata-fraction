
from app.services.fractionOperationStringValidator import FractionOperationStringValidator

def test_EmptyStringOperation_ShouldReturn_False():
  input:str = ""
  validatorResult:bool = FractionOperationStringValidator.Validate(input)
  assert validatorResult == False


def test_ValidFractionAddition_ShouldReturn_True():
  input:str = "4/3 + 2/3"
  validatorResult:bool = FractionOperationStringValidator.Validate(input)
  assert validatorResult == True