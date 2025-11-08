from flask import Blueprint

cart_module = Blueprint("cart",__name__,url_prefix="/cart")

from .cartdetails import *