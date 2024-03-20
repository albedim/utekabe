from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.schema.schema import UserAuthSchema, UserRefreshSchema, UserCompleteSchema, UserSigninSchema, TokenData
from app.services.user import UserService

userRouter: Blueprint = Blueprint('UserController', __name__, url_prefix="/users")


@userRouter.post("/signin")
def signin():
    return UserService.signin(request.json)

@userRouter.get("/<userId>/image")
def getImage(userId):
    return UserService.getImage(userId)

@userRouter.post("/create_password")
def createPassword():
    return UserService.createPassword(request.json)

@userRouter.post("/recover")
def recover():
    return UserService.recover(request.json)

@userRouter.post("/signup")
def signup():
    return UserService.signup(request.json)

@userRouter.get("/<libraryName>/analytics")
def getUserAnalytics(libraryName: str):
    return UserService.getAnalytics(request.args.get("filter"), libraryName)

@userRouter.put("/")
@jwt_required()
def update():
    return UserService.update(get_jwt_identity(), request.json)

@userRouter.get("/<userId>")
@jwt_required()
def getUser(userId: str):
    return UserService.getUser(get_jwt_identity(), userId)

@userRouter.get("/lib/<libraryName>")
def getUserByLibraryName(libraryName: str):
    return UserService.getUserByLibraryName(request.headers, libraryName)

@userRouter.get("/exists/<libraryName>")
def exists(libraryName: str):
    return UserService.exists(libraryName)

@userRouter.post("/sync")
@jwt_required()
def sync():
    return UserService.sync(get_jwt_identity())