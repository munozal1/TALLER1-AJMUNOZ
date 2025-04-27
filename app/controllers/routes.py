from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user, UserMixin
from app.models.users import user_db, User
from app.config.db import Perro
# from app import login_manager

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def index():
    #print("is auth 2:", current_user.username, current_user.is_authenticated)
    return render_template(
        "index.html",
        is_authenticated=current_user.is_authenticated,
        username=current_user.username if current_user.is_authenticated else None,
    )
    
@auth_bp.route('/dashboard_admin')
def dashboard_admin():
    Listaperros=Perro.query.all()
    return render_template(
        "dashboard_admin.html", perros=Listaperros,
        is_authenticated=current_user.is_authenticated,
        username=current_user.username if current_user.is_authenticated else None,
    )

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Busca el usuario en el diccionario
        user = user_db.get(username)
        print("Tipo:",type(user))
        print(user.username)
        if user and user.password == password:
            login_user(user)  # Inicia sesión
            print("is auth:", current_user.username, current_user.is_authenticated)
            flash("Inicio de sesión exitoso!","success")
            if user.is_admin:
                return redirect(url_for("auth.dashboard_admin"))
            else:
                return redirect(url_for("auth.index"))
        else:
            flash("Credenciales inválidas.")
    return render_template("login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Cierre de sesión exitoso!")
    return redirect(url_for("auth.index"))