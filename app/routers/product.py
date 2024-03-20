from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.routers.user import userRouter
from app.schema.schema import UserAuthSchema, UserRefreshSchema, UserCompleteSchema, UserSigninSchema, TokenData
from app.services.product import ProductService

productRouter: Blueprint = Blueprint('ProductController', __name__, url_prefix="/products")


@productRouter.post("/")
@jwt_required()
def create():
    return ProductService.create(get_jwt_identity(), request.json)

@productRouter.get("/user/<userId>")
def getProducts(userId: str):
    return ProductService.getProducts(userId)


@productRouter.get("/<productId>/file")
def getProduct(productId):
    return ProductService.getProduct(request.args.get("tk"), productId)

