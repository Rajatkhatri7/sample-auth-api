from fastapi import APIRouter, HTTPException,Depends
from models import Users,Profile
from database import get_db
from sqlalchemy.orm import Session



users_router = APIRouter(prefix="/users")


@users_router.post("/register", response_model=Users)
async def register_user(user: Users, db: Session = Depends(get_db)):
  # Check if the email and phone number already exist
  if db.query(Users).filter(Users.email == user.email).first():
    raise HTTPException(status_code=409, detail="Email already exists")
  elif(db.query(Users).filter(Users.phone == user.phone).first()):
    raise HTTPException(status_code=409, detail="Phone number already exists")

  # Create a new user
  new_user = Users(first_name=user.first_name, email=user.email, password=user.password, phone=user.phone)
  db.add(new_user)
  db.commit()

  new_profile = Profile(user_id=new_user.id)
  db.add(new_profile)
  db.commit()

  return new_user


