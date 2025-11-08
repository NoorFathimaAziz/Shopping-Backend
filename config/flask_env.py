from flask import Flask

def flask_config(app:Flask):
    app.config.update(
        SQLALCHEMY_DATABASE_URI = "postgresql://postgres:5432@localhost:5432/ecommerce",
        SQLALCHEMY_TRACK_MODIFICATIONS = False    
    )
    