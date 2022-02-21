from flask import redirect, render_template,request,flash,url_for,make_response,jsonify
from app_tienda import app,db
from app_tienda.models import users,product_category,products
from app_tienda.serializers import user_schema,users_schema,categoria_schema,categorias_schema,producto_schema,productos_schema
from flask_cors import cross_origin

@app.route('/index')
def index():
    template_name="index.html"
    usuarios=users.query.all()
    return render_template(template_name,usuarios=usuarios)

@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        uname=request.form["uname"]
        passw=request.form["passw"]
        login=users.query.filter_by(user_name=uname,password=passw).first()
        if login is not None:
            return redirect(url_for("index"))
        else:
            flash("Es Incorrecto el usuario o password")
            return redirect(url_for("login"))
    return render_template("login.html")    


@app.route("/registrar" , methods=["GET","POST"])
def registrar():
    if request.method=="POST":
        id=request.form['id']
        uname=request.form['uname']
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        phone_number=request.form['phone_number']
        passw=request.form['passw']
        new_usuario=users(id=id,user_name=uname,password=passw,first_name=first_name,last_name=last_name,phone_number=phone_number)
        db.session.add(new_usuario)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("registro.html")
            
            
#todo capa de servicios
@cross_origin
@app.route('/autenticar/<uname>/<passw>',methods=["POST"])
def autenticar(uname,passw):
    login=Usuarios.query.filter_by(user_name=uname,password=passw).first()
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
    id=request.json['id']
    uname=request.json['uname']
    first_name=request.json['first_name']
    last_name=request.json['last_name']
    phone_number=request.json['phone_number']
    passw=request.json['passw']
    new_usuario=users(id=id,username=uname,password=passw,first_name=first_name,last_name=last_name,phone_number=phone_number)
    db.session.add(new_usuario)
    db.session.commit()
    result=user_schema.dump(new_usuario)
    data ={
            'message':'Se Registro el usuario con exito',
            'status':200,
            'data':result
        }
    return make_response(jsonify(data))
    
@cross_origin
@app.route("/listar_usuarios",methods=["GET"])
def listar_usuarios():
    #todo seleccionado todos los objetos de la clase grupos
    usuarios=users.query.all()
    #todo serializando y seleccionado los atributos a cast en json
    #todo dump nos permite serializar los objetos de PYTHON 
    result=users_schema.dump(usuarios)
    
    #todo creando el documento de salida
    data={
        'message':'Todas mis usuarios',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

@cross_origin
@app.route("/add_categorias",methods=["POST"])
def add_categoria():
    id=request.json['id']
    name=request.json['name']
    description=request.json['description']
    new_categoria=product_category(id=id,name=name,description=description)
    db.session.add(new_categoria)
    db.session.commit()
    result=categoria_schema.dump(new_categoria)
    data ={
            'message':'Se Registro la categoria con exito',
            'status':200,
            'data':result
        }
    return make_response(jsonify(data))


@cross_origin
@app.route("/add_productos",methods=["POST"])
def add_productos():
    id=request.json['id']
    name=request.json['name']
    description=request.json['description']
    stock_code=request.json['stock_code']
    category_id=request.json['category_id']
    inventory_id=request.json['inventory_id']
    price=request.json['price']
    discount_id=request.json['discount_id']
    new_producto=products(id=id,name=name,description=description,stock_code=stock_code,category_id=category_id,inventory_id=inventory_id,price=price,discount_id=discount_id)
    db.session.add(new_producto)
    db.session.commit()
    result=producto_schema.dump(new_producto)
    data ={
            'message':'Se Registro el producto con exito',
            'status':200,
            'data':result
        }
    return make_response(jsonify(data))

@cross_origin
@app.route('/category_product/<int:categoryid>', methods=['GET'])
def category_product(categoryid):
    cate_product =product_category.query.get(categoryid)
    return jsonify(id=cate_product.id, name=cate_product.name, 
                description=cate_product.description,
                items=[dict(id=item.id,
        name=item.name, price=item.price,stock_code=item.stock_code) for item in
        cate_product.items])
            
            