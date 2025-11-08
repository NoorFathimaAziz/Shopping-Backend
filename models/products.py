from sqlalchemy import Integer , String , Column
from db import db

class Products(db.Model):
    __tablename__ = "products_table"
    prod_id = Column(Integer, primary_key=True)
    prod_name = Column(String(224), nullable=False)
    prod_price = Column(Integer, nullable=False)
    prod_desc = Column(String(224), nullable=False)
    Category = Column(String(224), nullable=False)
    prod_type = Column(String(224), nullable=False)
    discount = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    ratings = Column(Integer, nullable=False)
    prod_img = Column(String(224), nullable=False)


    