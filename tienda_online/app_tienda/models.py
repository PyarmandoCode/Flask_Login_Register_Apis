from app_tienda import db

class Usuarios(db.Model):
    cod_usuario=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(20))
    email =db.Column(db.String(20))
    password=db.Column(db.String(8))
    
    
#create SEQUENCE usuarios_id_seq;
#alter table usuarios alter column cod_usuario set default 
#nextval('usuarios_id_seq'::regclass)    