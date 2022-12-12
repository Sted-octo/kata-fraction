
from app.services.fractionOperationStringValidator import FractionOperationStringValidator

def test_empty_string_opperation_should_return_False():
  input:str = ""
  validatorResult:bool = FractionOperationStringValidator.Validate(input)
  assert validatorResult == False
