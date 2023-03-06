from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import relationship, backref
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '{mysql+pymysql}://{root}:*{senha}@{localhost}/{banco}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)

class Edificios(db.Model):
    __tablename__ = 'Edificios'
    id_edificio = db.Column('id_edificio', db.Integer, primary_key=True)
    bloco_edificio = db.Column('bloco_edificio', db.String(45))
    
    def __init__(self, id_edificio, bloco_edificio):
        self.id_edificio = id_edificio
        self.bloco_edificio = bloco_edificio
        
    def __repr__(self):
        return '<User %r>' % self.username
        
class Apartamentos(db.Model):
    __tablename__ = 'Apartamentos'
    nr_apartamento = db.Column('nr_apartamento', db.Integer, primary_key=True)
    mensalidade_apt = db.Column('mensalidade_apt', db.Float)
    disponibilidade = db.Column('disponibilidade', db.String(45))
    id_edificio_apt = db.Column('id_edificio_apt', db.ForeignKey('Edificios.id_edificio'))
    fk_edif = db.relationship("Edificios", backref=db.backref("edificios", uselist=False))
    
    def __init__(self, nr_apartamento, mensalidade_apt, disponibilidade, id_edificio_apt):
        self.nr_apartamento = nr_apartamento
        self.mensalidade_apt = mensalidade_apt
        self.disponibilidade = disponibilidade
        self.id_edificio_apt = id_edificio_apt
        
    def __repr__(self):
       return '<User %r>' % self.username
        
class Locatarios(db.Model):
    __tablename__ = 'Locatarios'
    nome_completo = db.Column('nome_completo', db.String(150))
    cpf = db.Column('cpf', db.String(20), primary_key=True)
    celular = db.Column('celular', db.String(20))
    mensalidade = db.Column('mensalidade', db.Float)
    id_edificio_loc = db.Column('id_edificio_loc', db.Integer)
    nr_apartamento_loc = db.Column('nr_apartamento_loc', db.ForeignKey('Apartamentos.nr_apartamento'))
    disponibilidade_apt = db.Column('disponibilidade_apt', db.String(20))
    fk_nr_apartamento_rel = db.relationship("Apartamentos", backref=db.backref("apartamentos", uselist=False))
    
    def __init__(self, nome_completo, cpf, celular, mensalidade, id_edificio_loc, nr_apartamento_loc, disponibilidade_apt):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.celular = celular
        self.mensalidade = mensalidade
        self.id_edificio_loc = id_edificio_loc
        self.nr_apartamento_loc = nr_apartamento_loc
        self.disponibilidade_apt = disponibilidade_apt
        
    def __repr__(self):
        return '<User %r>' % self.username 
    
with app.app_context():
    db.create_all()
    
@app.route("/")
def homepage():
    return render_template("home.html")
    

@app.route("/edificios", methods=['GET','POST'])
def edificios():
    if request.method == "GET":
        edificios = Edificios.query.all()
        return render_template("edificios.html", edificios=edificios)
        
    if request.method == "POST":
        edificios = Edificios(
            request.form['id_edificio'],
            request.form['bloco_edificio']
        )
        db.session.add(edificios)
        db.session.commit()
        return redirect(url_for("edificios"))
    return render_template("edificios.html")


@app.route("/apartamentos", methods=['GET', 'POST'])
def apartamentos():
    if request.method == "GET":
        apartamentos = Apartamentos.query.all()
        return render_template("apartamentos.html", apartamentos=apartamentos)
        
    if request.method == "POST":
        apartamentos = Apartamentos(
            request.form['nr_apartamento'],
            request.form['mensalidade'],
            request.form['disponibilidade'],
            request.form['id_edificio_apt']
        )
        db.session.add(apartamentos)
        db.session.commit()
        return redirect(url_for("apartamentos")) 
    return render_template("apartamentos.html")


@app.route("/locatarios", methods=["GET","POST"])
def locatarios():
    if request.method == "GET":
        locatarios = Locatarios.query.all()
        return render_template("locatarios.html", locatarios=locatarios)

    if request.method == "POST":
        locatarios = Locatarios(
            request.form['nome_completo'],
            request.form['cpf'],
            request.form['celular'],
            request.form['mensalidade'],
            request.form['id_edificio_loc'],
            request.form['nr_apartamento_loc'],
            request.form['disponibilidade_apt'],
        )
        db.session.add(locatarios)
        db.session.commit()
        return redirect(url_for("locatarios"))
    return render_template("locatarios.html")

if __name__ == "__main__":
    app.run(debug=True)