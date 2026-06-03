from pydantic import BaseModel
class contact(BaseModel):
    name:str
    phone:str
    email:str