from .route import user_module
from handlers import userhandler
from flask import request

@user_module.route('/userlist',methods = ['GET'])
def user_list():
    return userhandler().all_user()

@user_module.route('/createuser',methods = ['POST'])
def create_user():
    return userhandler().create_user(request=request)

@user_module.route('/deleteuser',methods = ['POST'])
def deleteuser():
    return userhandler().deleteuser(request=request)

@user_module.route('updateuser', methods = ['POST'])
def updateuser():
    return userhandler().updateuser(request=request)

@user_module.route('/getsingleuser', methods = ['POST'])
def getsingleuser():
    return userhandler().getsingleuser(request=request)