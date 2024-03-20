from app.configuration.config import sql
from app.model.entity.product import Product

class ProductRepository:

    @classmethod
    def getProducts(cls, userId):
        products = sql.session.query(Product).filter(Product.user_id == userId).all()
        return products

    @classmethod
    def create(cls, title, filePath, description, userId, typeId, cost):
        product = Product(title, filePath, description, userId, typeId, cost)
        sql.session.add(product)
        sql.session.commit()
        return product

    @classmethod
    def getProduct(cls, productId):
        product = sql.session.query(Product).filter(Product.product_id == productId).first()
        return product
