from flask import Blueprint
product_module = Blueprint("product",__name__,url_prefix='/product')

from .productdetails import *