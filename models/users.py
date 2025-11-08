from sqlalchemy import String,Column,Integer , DATE, CHAR
from db import db

class User(db.Model):
    __tablename__ = "user_details"
    user_id = Column(Integer , primary_key = True, autoincrement = True)
    user_name = Column( String(30) , nullable= False)
    user_address = Column(String(225), nullable=False)
    phn_no = Column(Integer ,nullable=False)
    email = Column(String, nullable=False)
    user_dob = Column(DATE, nullable=True)
    gender = Column(CHAR, nullable=False)
    prof_pic = Column(String, nullable= True)

