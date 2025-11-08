from sqlalchemy import Integer, String, Column, ForeignKey
from models import User , Products
from db import db

class Cart(db.Model):
    __tablename__ = "cart"
    relation_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.user_id))
    prod_id = Column(Integer , ForeignKey (Products.prod_id))



 