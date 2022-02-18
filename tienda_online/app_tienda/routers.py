

from flask import redirect, render_template,request,flash,url_for,make_response,jsonify
from app_tienda import app,db
from app_tienda.models import Usuarios
from app_tienda.serializers import user_schema,users_schema
from flask_cors import cross_origin

@app.route('/index')
def index():
    template_name="index.html"
    usuarios=Usuarios.query.all()
    return render_template(template_name,usuarios=usuarios)

@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        uname=request.form["uname"]
        passw=request.form["passw"]
        login=Usuarios.query.filter_by(username=uname,password=passw).first()
        if login is not None:
            return redirect(url_for("index"))
        else:
            flash("Es Incorrecto el usuario o password")
            return redirect(url_for("login"))
    return render_template("login.html")    


@app.route("/registrar" , methods=["GET","POST"])
def registrar():
    if request.method=="POST":
        uname=request.form['uname']
        mail=request.form['mail']
        passw=request.form['passw']
        new_usuario=Usuarios(username=uname,email=mail,password=passw)
        db.session.add(new_usuario)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("registro.html")
            
            
#todo capa de servicios
@cross_origin
@app.route('/autenticar/<uname>/<passw>',methods=["POST"])
def autemticar(uname,passw):
    login=Usuarios.query.filter_by(username=uname,password=passw).first()
    result=user_schema.dump(login)
    if login is not None:
        data ={
            'message':'Bienvenido',
            'status':200,
            'data':result
        }
    else:
        data ={
            'message':'Error',
            'status':200
            
        }
    return make_response(jsonify(data))  

@cross_origin
@app.route("/add_usuarios",methods=["POST"])
def add_usuarios():
    uname=request.json['uname']
    mail=request.json['mail']
    passw=request.json['passw']
    new_usuario=Usuarios(username=uname,email=mail,password=passw)
    db.session.add(new_usuario)
    db.session.commit()
    result=user_schema.dump(new_usuario)
    data ={
            'message':'Se Registro el usuario con exito',
            'status':200,
            'data':result
        }
    return make_response(jsonify(data))
    


            