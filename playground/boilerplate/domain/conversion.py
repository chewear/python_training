from pydantic import BaseModel, Field

class Conversion(BaseModel):
    source_currency: str = Field(min_length=3, max_length=3, description="Source Currency")
    target_currency: str = Field(min_length=3, max_length=3, description="Target Currency")
    amount_to_be_converted: float = Field(gt=0.0, description="Amount to be converted")
    converted_amount: float = Field(default=0.00, description="Converted Amount")