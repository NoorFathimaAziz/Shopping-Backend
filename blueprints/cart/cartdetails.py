from .route import cart_module
from handlers import carthandler
from db import db

@cart_module.route('/allcarts',methods = ["GET"])
def all_cart():
    return carthandler().all_cart()