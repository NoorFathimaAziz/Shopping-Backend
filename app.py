from flask import Flask
from config import flask_config
from db import *
from blueprints import user_module,product_module,order_module,transact_module,cart_module

def create_app() -> Flask:
    app:Flask = Flask(__name__)
    flask_config(app=app)
    init_db(app=app)
    app.register_blueprint(user_module)
    app.register_blueprint(product_module)
    app.register_blueprint(order_module)
    app.register_blueprint(transact_module)
    app.register_blueprint(cart_module)
    return app
   
  