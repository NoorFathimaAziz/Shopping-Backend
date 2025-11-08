from sqlalchemy import update, delete ,select
from models import User
from db import db
from flask import request

class userhandler:
    def __init__(self) -> None:
        self.session = db.session()

    def  all_user(self):
        try:
            stmt = select(User)
            result = self.session.execute(stmt).all()

            response = [{
                "id ":obj.user_id,
                "name ":obj.user_name,
                "address ":obj.user_address,
                "mob_num ":obj.phn_no,
                "email ":obj.email,
                "dob"  :obj.user_dob,
                "gender":obj.gender,
                "image":obj.prof_pic
                } 
            for obj, in result]
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
        
    def create_user(self,request):
        try:
            body = request.json
            user = User(
                user_name=body['user_name'],
                user_address = body['user_address'],
                phn_no = body['phn_no'],
                email= body['email'],
                user_dob = body['user_dob'],
                gender = body['gender'],
                prof_pic = body['prof_pic']
                )
            self.session.add(user)
            self.session.commit()
            return {
                "status":True,
                "error": 1,
                "message":"user added successfully"
            }
        except Exception as e:    
            return {
                "status": False,
                "error": 1,
                "message ": f' compilation Failed{e}'
            }    
    def deleteuser(self,request):
        try:
            body = request.json
            stmt = select(User).filter(User.user_id.in_([body['user_id']]))
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

    def updateuser(self,request):
        try:
            body = request.json
            stmt = update(User).where(User.user_id ==body['user_id']).values(**body)
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
        

    def getsingleuser(self,request):
        try:
            body = request.json
            stmt = select(User).where(User.user_id == body['user_id'])
            result = self.session.execute(stmt).one()

            if result:
                obj = result[0]
                return {
                    "status": True,
                    "error": 0,
                    "data": {
                        "id ":obj.user_id,
                        "name ":obj.user_name,
                        "address ":obj.user_address,
                        "mob_num ":obj.phn_no,
                        "email ":obj.email,
                        "dob"  :obj.user_dob,
                        "gender":obj.gender,
                        "image":obj.prof_pic
                    } ,
                    "message ": " compiled succesfully"
                }
            
            return {
                "status": True,
                "error": 3,
                "data": {},
                "message ": "user not availale"
            }
        except Exception as e:
            return{
                "status": False,
                "error": 1,
                "data":{},
                "message ": f' compilation Failed{e}'
            } 

            

