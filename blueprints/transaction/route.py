from flask import Blueprint

transact_module = Blueprint("transact",__name__,url_prefix="/transact")

from .transactiondetails import *