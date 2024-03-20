from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.routers.user import userRouter
from app.schema.schema import UserAuthSchema, UserRefreshSchema, UserCompleteSchema, UserSigninSchema, TokenData
from app.services.type import TypeService

typeRouter: Blueprint = Blueprint('TypeController', __name__, url_prefix="/types")

@typeRouter.get("/")
def getTypes():
    return TypeService.getTypes()
