from flask_jwt_extended import decode_token

from app.model.repository.product import ProductRepository
from app.model.repository.type import TypeRepository
from app.model.repository.order import OrderRepository
from app.model.repository.user import UserRepository
from app.utils.errors.GException import GException
from app.utils.errors.UserNotFoundException import UserNotFoundException
from app.utils.utils import createSuccessResponse, createErrorResponse


class OrderService:

    @classmethod
    def create(cls, headers, json):
        authUser = None
        if headers.get("Authorization") is not None:
            token = headers.get("Authorization").split(" ")[1]
            print(headers.get("Authorization"))
            try:
                auth = decode_token(token)['sub']
                authUser = UserRepository.getUserById(auth['user_id'])
            except Exception as exc:
                pass

        order = OrderRepository.create(authUser.user_id if authUser is not None else None, json['product_id'])
        return createSuccessResponse({
            'tk': order.tk
        })