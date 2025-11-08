from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

db:SQLAlchemy = SQLAlchemy()
migrate:Migrate = Migrate()

def init_db(app:Flask):
    db.init_app(app)
    migrate.init_app(app, db)

