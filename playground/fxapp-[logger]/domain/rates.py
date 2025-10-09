from pydantic import BaseModel, Field

class Rates(BaseModel):
    base: str = Field(min_length=3, max_length=3, description="Base Currency")
    date: str = Field(min_length=10, max_length=10, description="Date of Rates")
    rates: dict = Field(default={}, description="Rates Dictionary")