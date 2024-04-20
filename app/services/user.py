import datetime
import os
from datetime import timedelta

import jwt

from flask import send_file
from flask_jwt_extended import create_access_token, decode_token

from app.model.repository.order import OrderRepository
from app.model.repository.plan import PlanRepository
from app.model.repository.product import ProductRepository
from app.model.repository.user import UserRepository
from app.utils.errors.EmailNotSentException import EmailNotSentException
from app.utils.errors.FileNotFoundEcxeption import FileNotFoundException
from app.utils.errors.GException import GException
from app.utils.errors.InvalidSchemaException import InvalidSchemaException
from app.utils.errors.TokenExpiredException import TokenExpiredException
from app.utils.errors.UnAuthotizedException import UnAuthorizedException
from app.utils.errors.UserAlreadyExistsException import UserAlreadyExistsException
from app.utils.errors.UserNotFoundException import UserNotFoundException
from app.utils.schema import WELCOME_EMAIL, RECOVER_PASSWORD_EMAIL
from app.utils.utils import createSuccessResponse, createErrorResponse, hashString, saveFile, send_html_email, \
    getEmails, getVariables, BASE_FE_URL, generateUuid, generateFileName


class UserService:

    @classmethod
    def getUserByLibraryName(cls, headers, libraryName):
        try:
            authenticated = False
            authUser = None

            if headers.get("Authorization") is not None:
                token = headers.get("Authorization").split(" ")[1]
                try:
                    auth = decode_token(token)['sub']
                    authUser = UserRepository.getUserById(auth['user_id'])
                    authenticated = True
                except Exception as exc:
                    pass

            user = UserRepository.getUserByLibraryName(libraryName)
            plan = PlanRepository.getPlan(user.user_id)

            if user is None:
                raise UserNotFoundException()
            return createSuccessResponse(
                    user.toJSON(
                        own=False if not authenticated else authUser.user_id == user.user_id,
                        premium=plan.premium
                    )
            )
        except UserNotFoundException:
            return createErrorResponse(UserNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def getUser(cls, auth, userId):
        try:
            authUser = UserRepository.getUserById(auth['user_id'])
            if authUser is None:
                raise UnAuthorizedException()

            user = UserRepository.getUserById(userId)

            if user is None:
                raise UserNotFoundException()

            plan = PlanRepository.getPlan(user.user_id)

            return createSuccessResponse(
                user.toJSON(
                    own=authUser.user_id == user.user_id,
                    premium=plan.premium
                )
            )
        except UserNotFoundException:
            return createErrorResponse(UserNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def update(cls, auth, request):
        try:
            authUser = UserRepository.getUserById(auth['user_id'])
            if authUser is None:
                raise UnAuthorizedException()

            image = authUser.image_path
            if "http" not in request['image_path'] and request['image_path'] != "":
                imageName = generateFileName("png")
                image = f"files/images/users/{imageName}"
                saveFile(request['image_path'].split(",")[1], image)

            user = UserRepository.update(authUser, image, request)
            plan = PlanRepository.getPlan(user.user_id)

            return createSuccessResponse(
                user.toJSON(
                    own=True,
                    premium=plan.premium
                )
            )
        except UserNotFoundException:
            return createErrorResponse(UserNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def signin(cls, request):
        try:
            user = UserRepository.getUserByEmail(request['email'])

            if user is None:
                raise UserNotFoundException()
            if user.password == hashString(request['password']):
                return createSuccessResponse({
                    'token': create_access_token(
                        identity={'user_id': user.user_id, 'expires_in': 14},
                        expires_delta=timedelta(days=14)
                    ),
                    'expires_in': 14,
                    'library_name': user.library_name
                })
            else:
                raise UserNotFoundException()

        except UserNotFoundException as exc:
            return createErrorResponse(UserNotFoundException)
        except Exception as exc:
            print(exc)
            return createErrorResponse(GException(exc))

    @classmethod
    def exists(cls, args):
        user = None
        if args.get("libraryName") is not None:
            user = UserRepository.getUserByLibraryName(args.get("libraryName"))
        if args.get("email") is not None:
            user = UserRepository.getUserByEmail(args.get("email"))
        return createSuccessResponse(user is not None)

    @classmethod
    def sync(cls, tokenSub):
        try:
            user = UserRepository.getUserById(tokenSub['user_id'])
            if user is None:
                raise UserNotFoundException()
            return createSuccessResponse(True)
        except UserNotFoundException:
            return createErrorResponse(UserNotFoundException())
        except jwt.exceptions.ExpiredSignatureError:
            return createErrorResponse(TokenExpiredException())
        except jwt.exceptions.DecodeError:
            return createErrorResponse(UnAuthorizedException())
        except Exception as exc:
            print(exc)
            return createErrorResponse(GException(exc))

    @classmethod
    def signup(cls, request):
        try:
            user = UserRepository.getUserByEmail(request['email'])

            if user is not None:
                raise UserAlreadyExistsException()

            user = UserRepository.getUserByLibraryName(request['library_name'])

            if user is not None:
                raise UserAlreadyExistsException()

            imagePath = "files/images/users/default.png"
            if request['image'] != "":
                imageName = generateFileName("png")
                imagePath = f"files/images/users/{imageName}"
                saveFile(request['image'], imagePath)

            user = UserRepository.create(
                request['email'],
                request['name'],
                request['surname'],
                hashString(request['password']),
                imagePath,
                request['bio'],
                request['library_name'],
                request['city'],
                request['country'],
                request['paypal_email']
            )

            send_html_email(request['email'], getEmails("welcome")['title'].replace("{name}", user.name),
                            WELCOME_EMAIL.replace("{name}", user.name)
                            .replace("{BASE_FE_URL}", BASE_FE_URL))
            return createSuccessResponse({
                'token': create_access_token(identity={'user_id': user.user_id},
                                             expires_delta=timedelta(days=14)),
                'expires_in': 14
            })

        except UserAlreadyExistsException as exc:
            return createErrorResponse(UserAlreadyExistsException)
        except KeyError as exc:
            return createErrorResponse(InvalidSchemaException)
        except Exception as exc:
            print(exc)
            return createErrorResponse(GException(exc))

    @classmethod
    def getMatchingUsers(cls, auth, name):
        try:
            user = UserRepository.getUserById(auth['user_id'])
            if user is None:
                raise UserNotFoundException

            users = UserRepository.getUsers(user.user_id, name)
            res = []
            for user in users:
                res.append(user.toJSON())
            return createSuccessResponse(res)
        except UserNotFoundException:
            return createErrorResponse(UnAuthorizedException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def change(cls, auth, request):
        try:
            userId = auth['user_id']
            user = UserRepository.getUserById(userId)

            if user is None:
                raise UserNotFoundException()

            password = hashString(request['password']) if request['password'] != "" else hashString(user.password)
            bio = request['bio'] if request['bio'] != "" else None
            UserRepository.change(user, bio, password)

            return createSuccessResponse("changed")
        except UserNotFoundException:
            return createErrorResponse(UserNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def recover(cls, request):
        try:
            user = UserRepository.getUserByEmail(request['email'])

            if user is None:
                raise UserNotFoundException()

            recoveryToken = UserRepository.createRecoveryToken(user)
            send_html_email(user.email, getEmails("recover_password")['title'],
                        RECOVER_PASSWORD_EMAIL.replace("{name}", user.name)
                        .replace("{RECOVER_URL}", f"{BASE_FE_URL}/create_password?token={recoveryToken}"))
            return createSuccessResponse("An email to recover your password was sent to you")

        except UserNotFoundException:
            return createErrorResponse(UserNotFoundException)
        except EmailNotSentException:
            return createErrorResponse(EmailNotSentException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def createPassword(cls, request):
        try:
            user = UserRepository.getUserByRecoveryToken(request['recovery_token'])

            if user is None:
                raise UserNotFoundException()

            if request['password'] != request['password_confirmation']:
                raise UnAuthorizedException()

            UserRepository.createPassword(user, hashString(request['password']))
            return createSuccessResponse("created")
        except UserNotFoundException:
            return createErrorResponse(UserNotFoundException)
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def getAnalytics(cls, filter, libraryName):
        user = UserRepository.getUserByLibraryName(libraryName)

        if user is None:
            raise UserNotFoundException()

        products = len(ProductRepository.getProducts(user.user_id))
        sold_products = len(OrderRepository.getOrders(user.user_id))
        earnings = OrderRepository.getEarnings(user.user_id)[0]
        created_on = (datetime.date.today() - user.created_on).days + 1

        graph = OrderRepository.getOrdersGraph(filter, user.user_id)
        x = [e[1] for e in graph]
        y = [e[0] for e in graph]
        res = cls.fill(x, y, filter)

        graph = OrderRepository.getEarningsGraph(filter, user.user_id)
        x = [e[1] for e in graph]
        y = [int(e[0]) for e in graph]
        res1 = cls.fill(x, y, filter)

        return createSuccessResponse({
            "products": products,
            "sold_products": sold_products,
            "earnings": int(earnings) if earnings is not None else 0,
            "created_on": created_on,
            "graph": {
                "x": res[0],
                "y": res[1]
            },
            "graph1": {
                "x": res1[0],
                "y": res1[1]
            },
        })

    @classmethod
    def fill(cls, list1, list2, period):
        periods = {
            'day': ["01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00",
                    "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00",
                    "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00",
                    "23:00", "24:00"],
            'week': ["Domenica", "Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato"],
            'month': [str(i) for i in range(1, 32)],
            'year': ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio",
                     "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]
        }

        values = periods.get(period.lower())
        x = values
        y = [0] * len(x)
        for e in list1:
            y[e - 1] = list2[list1.index(e)]

        return x, y
    @classmethod
    def getImage(cls, userId):
        try:
            user = UserRepository.getUserById(userId)
            if user is None:
                raise UserNotFoundException()
            return send_file(os.path.abspath(user.image_path), mimetype='image/png')
        except UserNotFoundException:
            return createErrorResponse(UserNotFoundException())
        except FileNotFoundException:
            return createErrorResponse(FileNotFoundException())
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def changePlan(cls, auth, request):

        user = UserRepository.getUserById(auth['user_id'])
        if user is None:
            raise UserNotFoundException()

        plan = PlanRepository.getPlanById(request['plan_id'])
        if plan is None:
            raise UnAuthorizedException()

        userPlan = PlanRepository.getPlan(user.user_id)
        if not plan.premium or userPlan.plan_id >= plan.plan_id:
            raise UnAuthorizedException()

        PlanRepository.changePlan(user, plan.plan_id)
        return createSuccessResponse("created")

