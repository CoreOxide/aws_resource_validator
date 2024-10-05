from pydantic import BaseModel

class BaseValidatorModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True
