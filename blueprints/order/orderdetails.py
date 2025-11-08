from flask import request
from handlers import ordershandler
from .route import order_module

@order_module.route('/allorders', methods = ['GET'])
def all_order():
    return ordershandler().getorders()

@order_module.route('/createorder', methods = ['POST'])
def create_order():
    return ordershandler().createorders(request=request)