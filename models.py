from pydantic import BaseModel

class Users (BaseModel):
  user_id: str
  full_name: str
  email: str
  password: str
  phone: str

class Profile(BaseModel):
  id: int
  user_id: str
  profile_picture: str
