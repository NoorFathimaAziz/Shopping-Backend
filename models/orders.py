from sqlalchemy import String , Integer ,Column , ForeignKey , Date
from models import Products , User , Transaction
from db import db 

class orders(db.Model):
    __tablename__ = "order_details"

    ord_id = Column(Integer, primary_key=True , autoincrement= True)
    prod_id = Column( Integer ,ForeignKey(Products.prod_id))
    user_id = Column( Integer , ForeignKey(User.user_id))
    prod_status = Column( String(25))
    deli_date = Column( Date, nullable= False)
    trans_id = Column( Integer , ForeignKey(Transaction.trans_id))
    deli_status = Column( String , nullable= False) 