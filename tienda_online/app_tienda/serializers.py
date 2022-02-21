from app_tienda import app

from app_tienda.models import users,product_category,products
from flask_marshmallow import Marshmallow

ma=Marshmallow(app)

class UserSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=users
        fields=('id','username','first_name','last_name','phone_number','password')
        
user_schema=UserSerializer()
users_schema=UserSerializer(many=True)        


class CategoriaSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=product_category
        fields=('id','name','description')
        
categoria_schema=CategoriaSerializer()
categorias_schema=CategoriaSerializer(many=True)  

class ProductosSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=products
        fields=('id','name','description','stock_code','category_id','inventory_id','price','discount_id')
        
producto_schema=ProductosSerializer()
productos_schema=ProductosSerializer(many=True)  
        
   