from pydantic import BaseModel, Field

class Contact(BaseModel):
    name: str = Field(default="Default Name", min_length=1, max_length=20)
    contact_number: str = Field(default="000000000", min_length=1, max_length=20)