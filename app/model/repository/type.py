from app.configuration.config import sql
from app.model.entity.type import Type

class TypeRepository:

    ...

    @classmethod
    def getType(cls, type_id):
        type = sql.session.query(Type).filter(Type.type_id == type_id).first()
        return type

    @classmethod
    def getTypes(cls):
        types = sql.session.query(Type).all()
        return types