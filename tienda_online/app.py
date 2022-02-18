from app_tienda import app

#todo es el nombre el entorno en cua se ejecuta el codigo
#todo de maximo nivel . es el primer modulo de nuestra app
if __name__=='__main__':
    app.run(debug=True)
    
# mk tienda_online
# py -m venv . 


#pip install flask flask_restful flask_sqlalchemy flask_marshmallow marshmallow-sqlalchemy flask-cors psycopg2-binary pymysql gunicorn