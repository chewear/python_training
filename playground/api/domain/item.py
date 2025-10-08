from pydantic import BaseModel, Field

class Item(BaseModel):
    item_id:int
    item_name:str = Field(default="sample item", min_length=10)