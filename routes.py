from fastapi import APIRouter, HTTPException,Depends
from models import CreateUser,ResponseModel
from database import get_db
from sqlalchemy.orm import Session
from schema import Users,Profile
import base64
import uuid


users_router = APIRouter(prefix="/users")


@users_router.post("/register", response_model=ResponseModel)
async def register_user(user: CreateUser, db: Session = Depends(get_db)):
  # Check if the email and phone number already exist
  if db.query(Users).filter(Users.email == user.email).first():
    raise HTTPException(status_code=409, detail="Email already exists")
  elif(db.query(Users).filter(Users.phone == user.phone).first()):
    raise HTTPException(status_code=409, detail="Phone number already exists")

  

  try:


    image_bytes = base64.b64decode(user.profile)
    # Create a new user
    new_user = Users(user_id= str(uuid.uuid4()), full_name=user.full_name, email=user.email, password=user.password, phone=user.phone)
    db.add(new_user)
    db.commit() 
  
    new_profile = Profile(user_id=new_user.user_id,profile_picture=image_bytes)
    db.add(new_profile)
    db.commit()
    
    return ResponseModel(status="success",message="Registered Successfully",data={"user_id":new_user.user_id})
  
  except Exception as err:
    db.rollback()
    return ResponseModel(status="failed",message=err,data={})



@users_router.get("/user/{user_id}",response_model=ResponseModel)
async def get_user(user_id: str, db: Session = Depends(get_db)):
  user = db.query(Users).filter(Users.user_id == user_id).first()
  if user is None:
    raise HTTPException(status_code=404, detail="User not found")

  profile = db.query(Profile).filter(Profile.user_id==user_id).first()
  image_data_base64 = base64.b64encode(profile.profile_picture).decode('utf-8')

  data = {
    "full_name":user.full_name,
    "email":user.email,
    "phone":user.phone,
    "profile":image_data_base64,
  }

  return ResponseModel(status="success",message="Users details fetched successfully",data={"userDetails":data})



