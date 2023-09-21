from pydantic import BaseModel

class CreateUser(BaseModel):
  full_name: str
  email: str
  password: str
  phone: str
  profile:str


class ResponseModel(BaseModel):
  status:str
  message:str
  data:dict
