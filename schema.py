from database import Base
from sqlalchemy import Column,ForeignKey,Integer,String,Boolean

class Users(Base):

    __tablename__= "users"


    user_id = Column(String, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    phone = Column(String(20), unique=True, nullable=False)


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String,ForeignKey("users.user_id"))
    profile_picture = Column(String,nullable=False)