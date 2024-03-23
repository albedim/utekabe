from app.configuration.config import sql
from app.utils.utils import BASE_URL, generateUuid


class Product(sql.Model):
    __tablename__ = "products"
    product_id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey("users.user_id"), nullable=False)
    file_path = sql.Column(sql.String, nullable=False)
    hidden = sql.Column(sql.Boolean, nullable=False, default=False)
    title = sql.Column(sql.String(64), nullable=False)
    description = sql.Column(sql.String(100), nullable=False)
    type_id = sql.Column(sql.Integer, sql.ForeignKey("types.type_id"), nullable=False)
    cost = sql.Column(sql.Integer, nullable=False)

    def __init__(self, title, filePath, description, userId, type_id, cost):
        self.title = title
        self.hidden = False
        self.file_path = filePath
        self.description = description
        self.user_id = userId
        self.type_id = type_id
        self.cost = cost

    def toJSON(self, **kvargs):
        obj = {
            'product_id': self.product_id,
            'title': self.title,
            'file_path': f"{BASE_URL}/products/{self.product_id}/file",
            'user_id': self.user_id,
            'hidden': self.hidden,
            'description': self.description,
            'type_id': self.type_id,
            'cost': self.cost
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj