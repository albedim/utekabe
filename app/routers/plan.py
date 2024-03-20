from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.routers.user import userRouter
from app.schema.schema import UserAuthSchema, UserRefreshSchema, UserCompleteSchema, UserSigninSchema, TokenData
from app.services.plans import PlanService

planRouter: Blueprint = Blueprint('PlanController', __name__, url_prefix="/plans")

@planRouter.get("/")
def plans():
    return PlanService.getPlans()