from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.routers.user import userRouter
from app.schema.schema import UserAuthSchema, UserRefreshSchema, UserCompleteSchema, UserSigninSchema, TokenData
from app.services.order import OrderService
from app.services.review import ReviewService

reviewRouter: Blueprint = Blueprint('ReviewController', __name__, url_prefix="/reviews")


@reviewRouter.get("/")
def get():
    return ReviewService.getReviews()


@reviewRouter.post("/")
@jwt_required()
def create():
    return ReviewService.create(get_jwt_identity(), request.json)