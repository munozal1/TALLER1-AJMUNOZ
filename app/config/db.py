from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class Cuidador(db.Model):
    
    __tablename__='cuidadores'
    
    Id=db.Column(db.Integer, primary_key = True)
    Nombre=db.Column(db.Integer, primary_key = True)
    Telefono=db.Column(db.String(50),nullable=False)

class Perro(db.Model):
    
    __tablename__= 'perros'
    
    Id = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column(db.String(50), nullable=False)
    Raza = db.Column(db.String(50),nullable=False)
    Edad = db.Column(db.Integer,nullable=False)
    Peso = db.Column(db.Float,nullable=False)
    Id_Cuidador = db.Column(db.Integer, db.ForeignKey(Cuidador.Id), nullable=False)
