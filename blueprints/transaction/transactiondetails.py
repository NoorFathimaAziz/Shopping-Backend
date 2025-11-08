from flask import request
from handlers import transacthandler
from .route import transact_module

@transact_module.route('/alltransactions',methods = ["GET"])
def all_transaction():
    return transacthandler().all_transact()