from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
  full_name: str
  email: EmailStr
  password: str
  phone: str
  profile:str


class ResponseModel(BaseModel):
  status:str
  message:str
  data:dict
