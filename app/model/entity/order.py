import datetime

from app.configuration.config import sql
from app.utils.utils import generateUuid


class Order(sql.Model):
    __tablename__ = "orders"
    order_id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    user_id = sql.Column(sql.BigInteger, sql.ForeignKey("users.user_id"), nullable=True)
    tk = sql.Column(sql.String(50), nullable=True)
    created_on = sql.Column(sql.DateTime, nullable=False)
    product_id = sql.Column(sql.Integer, sql.ForeignKey("products.product_id"), nullable=False)

    def __init__(self, userId, productId):
        self.user_id = userId
        self.tk = generateUuid(50)
        self.product_id = productId
        self.created_on = datetime.datetime.now()

    def toJSON(self, **kvargs):
        obj = {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'created_on': self.created_on.strftime("%Y-%m-%d"),
            'product_id': self.product_id
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj