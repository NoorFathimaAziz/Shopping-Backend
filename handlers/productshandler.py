from models import Products
from db import db
from sqlalchemy import select , update,delete
from flask import request


class productshandler:
    def __init__(self) -> None:
        self.session = db.session()

    def all_products(self):
        try:
            stmt = select(Products)
            result = self.session.execute(stmt).all()

            response = [{
                        "id" : obj.prod_id,
                        "product-name": obj.prod_name,
                        "price(after discount) ": (obj.prod_price * (100 - obj.discount))/100 ,
                        "description": obj.prod_desc,
                        "Category": obj.Category,
                        "type":obj.prod_type,
                        "discount":f'{obj.discount} %',
                        "weight":f'{obj.weight} gm',
                        "ratings":f'{obj.ratings} stars',
                        "image":obj.prod_img
                        } 
                        for obj, in result
                        ]
            return {
                "status": True,
                "error": 0,
                "data": response,
                "message ": " compiled succesfully"
            }
        except Exception as e:
            return {
                "status": False,
                "error": 1,
                "data":[],
                "message ": f' compilation Failed{e}'
            } 
        
    def add_products(self,request):
        try:
            body = request.json
            product = Products(
                prod_name = body['prod_name'],
                prod_price = body['prod_price'],
                prod_desc = body['prod_desc'],
                Category = body['Category'],
                prod_type = body['prod_type'],
                discount = body['discount'],
                weight = body['weight'] ,
                ratings = body['ratings'],
                prod_img = body['prod_img']

            )
            self.session.add(product)
            self.session.commit()
            return {
                "status": True,
                "error": 0,
                "message": "product added succesfully"
            }
        except Exception as e:
            return {
                "status": False,
                "error": 5,
                "message": f"product addition was  unsuccesfull {e}"
            }

    def delete_products(self,request):
        try:
            body = request.json
            stmt = select(Products).filter(Products.prod_id.in_([body['prod_id']]))
            result = self.session.execute(stmt).all()
            if len(result)== 0:
                    return {
                        "status" : False,
                        "error"  : 1,
                        "message" : "its already empty"
                    }
            for obj, in result:
                    self.session.delete(obj)
            self.session.commit()  
            return {
                    "status":True,
                    "error":0,
                    "message":"deleted successfully"
                } 

        except Exception as e:
            return {
                "status":False,
                "error":1,
                "message":f"deletion was not possible {e}"
            }
    def update_products(self,request):
        try:
            body = request.json
            stmt = update(Products).where(Products.prod_id ==body['prod_id']).values(**body)
            print(stmt)
            self.session.execute(stmt)
            self.session.commit()
            return {
                "status":True,
                "error":0,
                "message":"updated successfully"
            } 

        except Exception as e:
            return {
                "status": False,
                "error":1,
                "message": f"updating caused an error as {e}"
            }     
            

    def getsingleproducts(self,request):
        try:
            body = request.json
            stmt = select(Products).where(Products.prod_id == body['prod_id'])
            result = self.session.execute(stmt).one()

            if result:
                obj = result[0]
                return {
                    "status": True,
                    "error": 0,
                    "data": {
                        "id" : obj.prod_id,
                        "product-name": obj.prod_name,
                        "price(after discount) ": (obj.prod_price * (100 - obj.discount))/100 ,
                        "description": obj.prod_desc,
                        "Category": obj.Category,
                        "type":obj.prod_type,
                        "discount":f'{obj.discount} %',
                        "weight":f'{obj.weight} gm',
                        "ratings":f'{obj.ratings} stars',
                        "image":obj.prod_img
                        }  ,
                    "message ": " compiled succesfully"
                }
            
            return {
                "status": True,
                "error": 3,
                "data": {},
                "message ": "prod not availale"
            }
        except Exception as e:
            return{
                "status": False,
                "error": 1,
                "data":{},
                "message ": f' compilation Failed{e}'
            }             

