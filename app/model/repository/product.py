from app.configuration.config import sql
from app.model.entity.product import Product

class ProductRepository:

    @classmethod
    def getProducts(cls, userId):
        products = sql.session.query(Product).filter(Product.user_id == userId).filter(Product.hidden == False).all()
        return products

    @classmethod
    def create(cls, title, filePath, description, timeToRead, userId, typeId, cost):
        product = Product(title, filePath, description, timeToRead, userId, typeId, cost)
        sql.session.add(product)
        sql.session.commit()
        return product

    @classmethod
    def getProduct(cls, productId):
        product = sql.session.query(Product).filter(Product.product_id == productId).first()
        return product

    @classmethod
    def removeProduct(cls, productId):
        sql.session.query(Product).filter(Product.product_id == productId).delete()
        sql.session.commit()

    @classmethod
    def hideProduct(cls, product):
        product.hidden = True
        sql.session.commit()

    @classmethod
    def getHiddenProducts(cls, userId):
        products = sql.session.query(Product).filter(Product.user_id == userId).filter(Product.hidden == True).all()
        return products

    @classmethod
    def unhideProduct(cls, product):
        product.hidden = False
        sql.session.commit()
