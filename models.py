from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
  full_name: str
  email: EmailStr
  password: str
  phone: str
  profile:bytes


class ResponseModel(BaseModel):
  status:str
  message:str
  data:dict
