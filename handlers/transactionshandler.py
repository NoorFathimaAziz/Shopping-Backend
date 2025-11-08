from flask import request
from db import db
from sqlalchemy import select ,update , delete
from models import Transaction

class transacthandler:
    def __init__(self) -> None:
         self.session  = db.session()
    def all_transact(self):
        try:
            stmt = select(Transaction)
            result = self.session.execute(stmt).all()
            response = [{
                "trans_id" : obj.trans_id,
                "mode of transact":obj.trans_type,
                "trans_date":obj.trans_date,
                "trans_status":obj.trans_status,
                "user_id": obj.user_id

            } for obj, in result]
            return {
                "status": True,
                "error":0,
                "data": response,
                "message":"transactions fetched successfully"
            }
        except Exception as e:
            return {
                "status": False,
                "error":9,
                "data": [],
                "message":f"failed to provide transaction {e}"
            }
                      