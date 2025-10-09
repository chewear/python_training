from pydantic import Field, BaseModel
from typing import Optional, TypeVar, Generic

T = TypeVar("T", bound=BaseModel)

class ServiceResponse(BaseModel, Generic[T]):
    status_code:int = Field(default=200, description="API Response Status Code")
    status_message:str = Field(default="success", description="API Response Description")
    data:Optional[T] = Field(description="API Response Data", default=None)