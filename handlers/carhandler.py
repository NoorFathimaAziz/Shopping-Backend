from models import Cart
from db import db
from flask import request
from sqlalchemy import select

class carthandler:
    def __init__(self) -> None:
        self.session = db.session()

    def all_cart(self):
        try:
            stmt = select(Cart)
            result = self.session.execute(stmt).all()
            response = [{
                "relation_id":obj.relation_id,
                "user_id":obj.user_id,
                "prod_id":obj.prod_id

            }for obj, in result]
            return {
                "status":True,
                "error":0,
                "data":response,
                "message":"cart items displayed successfully"
            }
        except Exception as e:
            return {
                "status":False,
                "error":9,
                "data":[],
                "message":f"cerror fetching cart items as {e}"
            }
        








# class Coursehandler(self):
#     def __init__(self):
#         self.session = db.session()
#     def all_course(self):
#         try:
#             stmt = session(Course)
#             res = self.session.execute(stmt).all()
#             response = [{
#                 "course_id" : obj.course_id,
#                 "course_name": obj.course_name,
#                 "course_credit" : obj.course_credit,
#                 "course_fee":obj.course_fee
#             }for obj, in res]
#             return{
#                 "status":True,
#                 "error":0,
#                 "data":response,
#                 "message":"all courses displayed successfully!"
#             }
#         except Exception as e:
#             return{
#                 "status":False,
#                 "error":1,
#                 "data": [],
#                 "message": f"error, fetching course as {e}"
#             }







