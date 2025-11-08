from sqlalchemy import select , update , delete 
from models import orders
from flask import request
from db import db

class ordershandler:
    def __init__(self) -> None:
        self.session = db.session()

    def getorders(self):
        try:
            stmt = select(orders)
            result = self.session.execute(stmt).all()
            response =[ {
                "order_id":obj.ord_id,
                "prod_id":obj.prod_id,
                "user_id":obj.user_id,
                "status":obj.prod_status,
                "delivery date":obj.deli_date,
                "trans_id":obj.trans_id,
                "deli_status":obj.deli_status
            } for obj, in result]
            return{
                "status":True,
                "error":0,
                "data":response,
                "message":" all orders are dispplayed successfully"
            }
        except Exception as e:
            return{
                "status":False,
                "error":5,
                "data":[],
                "message":f'orders dislpay failed as {e}'
            }
        
    def createorders(self,request):
        try:
            body = request.json
            order = orders(
                prod_id=body['prod_id'],
                user_id=body['user_id'],
                prod_status=body['prod_status'],
                deli_date=body['deli_date'],
                trans_id = body['trans_id'],
                deli_status = body['deli_status']
            )    
            self.session.add(order)
            self.session.commit()
            return {
                "status":True,
                "error":0,
                "message":"orders added succesfully"
            }
            
        except Exception as e:
            return {
                "status":False,
                "error":5,
                "message":f'orders dislpay failed as {e}'
            }    