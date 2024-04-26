import os

from fitz import fitz
from flask import send_file, request
from app.model.repository.order import OrderRepository
from app.model.repository.product import ProductRepository
from app.model.repository.type import TypeRepository
from app.model.repository.user import UserRepository
from app.utils.errors.GException import GException
from app.utils.errors.UnAuthotizedException import UnAuthorizedException
from app.utils.errors.UserNotFoundException import UserNotFoundException
from app.utils.utils import createSuccessResponse, createErrorResponse, saveFile, generateUuid, generateFileName


class ProductService:

    @classmethod
    def create(cls, auth, request):
        try:
            user = UserRepository.getUserById(auth['user_id'])
            if user is None:
                raise UserNotFoundException()

            fileName = "files/products/" + generateFileName("pdf")
            saveFile(request['file'], fileName)
            timeToRead = cls.getTimeToRead(fileName)
            product = ProductRepository.create(
                request['title'],
                fileName,
                request['description'],
                timeToRead,
                user.user_id,
                request['type_id'],
                request['cost']
            )
            return createSuccessResponse("created")
        except UserNotFoundException as exc:
            return createErrorResponse(UserNotFoundException)
        except Exception as exc:
            print(exc)
            return createErrorResponse(GException(exc))

    @classmethod
    def getTimeToRead(cls, fileName):
        doc = fitz.open(os.path.abspath(fileName))  # open a document
        length = 0
        for page in doc:
            length += len(page.get_text())
        return length / 200 * 60

    @classmethod
    def getProducts(cls, userId):
        try:
            user = UserRepository.getUserById(userId)
            if user is None:
                raise UserNotFoundException()
            products = [
                product.toJSON(type=TypeRepository.getType(product.type_id).toJSON())
                for product in ProductRepository.getProducts(userId)
            ]
            return createSuccessResponse(products)
        except UserNotFoundException as exc:
            return createErrorResponse(UserNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def deleteProduct(cls, auth, productId):
        try:
            user = UserRepository.getUserById(auth['user_id'])

            if user is None:
                raise UserNotFoundException()

            product = ProductRepository.getProduct(productId)

            if product is None or product.user_id != user.user_id:
                raise UnAuthorizedException()

            ProductRepository.removeProduct(product.product_id)
            return createSuccessResponse("removed")
        except UserNotFoundException as exc:
            return createErrorResponse(UserNotFoundException)
        except UnAuthorizedException as exc:
            return createErrorResponse(UnAuthorizedException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def getHiddenProducts(cls, userId):
        try:
            user = UserRepository.getUserById(userId)
            if user is None:
                raise UserNotFoundException()
            products = [
                product.toJSON(type=TypeRepository.getType(product.type_id).toJSON())
                for product in ProductRepository.getHiddenProducts(userId)
            ]
            return createSuccessResponse(products)
        except UserNotFoundException as exc:
            return createErrorResponse(UserNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def getProduct(cls, tk, productId):
        try:
            order = OrderRepository.getOrderByTk(tk)
            if order is None:
                raise UnAuthorizedException()
            product = ProductRepository.getProduct(productId)
            return send_file(os.path.abspath(product.file_path), mimetype="application/pdf", as_attachment=True)
        except UserNotFoundException as exc:
            return createErrorResponse(UserNotFoundException(exc))
        except UnAuthorizedException as exc:
            return createErrorResponse(UnAuthorizedException(exc))
        except Exception as exc:
            print(exc)
            return createErrorResponse(GException(exc))

    @classmethod
    def unhideProduct(cls, auth, request):
        try:
            user = UserRepository.getUserById(auth['user_id'])

            if user is None:
                raise UserNotFoundException()

            product = ProductRepository.getProduct(request['product_id'])

            if product is None:
                raise UnAuthorizedException()
            ProductRepository.unhideProduct(product)
            products = [
                product.toJSON(type=TypeRepository.getType(product.type_id).toJSON())
                for product in ProductRepository.getProducts(user.user_id)
            ]
            return createSuccessResponse(products)
        except UserNotFoundException as exc:
            return createErrorResponse(UserNotFoundException)
        except Exception as exc:
            print(exc)
            return createErrorResponse(GException(exc))

    @classmethod
    def hideProduct(cls, auth, request):
        try:
            user = UserRepository.getUserById(auth['user_id'])

            if user is None:
                raise UserNotFoundException()

            product = ProductRepository.getProduct(request['product_id'])

            if product is None:
                raise UnAuthorizedException()
            ProductRepository.hideProduct(product)
            products = [
                product.toJSON(type=TypeRepository.getType(product.type_id).toJSON())
                for product in ProductRepository.getProducts(user.user_id)
            ]
            return createSuccessResponse(products)
        except UserNotFoundException as exc:
            return createErrorResponse(UserNotFoundException)
        except Exception as exc:
            print(exc)
            return createErrorResponse(GException(exc))