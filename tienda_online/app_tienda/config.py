#pip install psycopg2-binary
class Config(object):
    #todo conectand a la base de datos de POSTGRESS modificado el dialecto
    #todo conectado a la base de datos de MYSQL
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/ecommerce_cargamos'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:rioazulq12@localhost:5432/ecommerce_cargamos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True