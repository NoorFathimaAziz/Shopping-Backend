from sqlalchemy import String, Integer, Column,Date, ForeignKey
from models import User
from db import db

class Transaction(db.Model):
    __tablename__ = "transactions"

    trans_id = Column(Integer, primary_key=True, autoincrement=True)
    trans_type = Column(String)
    trans_date = Column(Date)
    trans_status = Column(String)
    user_id = Column(Integer, ForeignKey(User.user_id))
