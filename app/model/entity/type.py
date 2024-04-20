from app.configuration.config import sql


class Type(sql.Model):
    __tablename__ = "types"
    type_id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    name = sql.Column(sql.String(24), nullable=False)

    def __init__(self, name):
        self.name = name

    def toJSON(self, **kvargs):
        obj = {
            'type_id': self.type_id,
            'name': self.name
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj