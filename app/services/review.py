from flask_jwt_extended import decode_token

from app.model.repository.product import ProductRepository
from app.model.repository.review import ReviewRepository
from app.model.repository.type import TypeRepository
from app.model.repository.order import OrderRepository
from app.model.repository.user import UserRepository
from app.utils.errors.GException import GException
from app.utils.errors.UnAuthotizedException import UnAuthorizedException
from app.utils.errors.UserNotFoundException import UserNotFoundException
from app.utils.utils import createSuccessResponse, createErrorResponse


class ReviewService:

    @classmethod
    def getReviews(cls):
        try:
            reviews = ReviewRepository.getReviews()
            reviews = [review.toJSON(user=UserRepository.getUserById(review.user_id).toJSON()) for review in reviews]
            return createSuccessResponse(reviews)
        except GException as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def create(cls, auth, request):
        try:
            user = UserRepository.getUserById(auth['user_id'])

            if user is None:
                raise UserNotFoundException()

            if request['stars'] < 1 or request['stars'] > 5:
                raise UnAuthorizedException()

            review = ReviewRepository.create(user.user_id, request['content'], request['stars'])
            return createSuccessResponse(review.toJSON())
        except UnAuthorizedException as exc:
            return createErrorResponse(UnAuthorizedException)
        except UserNotFoundException as exc:
            return createErrorResponse(UserNotFoundException)
        except GException as exc:
            return createErrorResponse(GException(exc))