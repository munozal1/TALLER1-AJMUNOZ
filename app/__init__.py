from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.models.users import User,user_db
from app.controllers.routes import auth_bp
from app.config.db import db

#db = SQLAlchemy()

login_manager = LoginManager()

def create_app(config_class):
    app = Flask(__name__, template_folder="views")
    app.config.from_object(config_class)

    # Inicializa extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Registra el blueprint de autenticación
    app.register_blueprint(auth_bp)

    # Crea las tablas
    with app.app_context():
        db.create_all()

    return app

@login_manager.user_loader
def load_user(user_id):
    print("user id:", user_id)
    for user in user_db:
        if user_db.get(user).id==int(user_id):    
            print(user_db)
            return user_db.get(user)
    return None
