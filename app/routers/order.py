from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.routers.user import userRouter
from app.schema.schema import UserAuthSchema, UserRefreshSchema, UserCompleteSchema, UserSigninSchema, TokenData
from app.services.order import OrderService

orderRouter: Blueprint = Blueprint('OrderController', __name__, url_prefix="/orders")

@orderRouter.post("/")
def create():
    return OrderService.create(request.headers, request.json)