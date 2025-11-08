from flask import Blueprint

order_module = Blueprint("order",__name__,url_prefix='/order')

from .orderdetails import *
