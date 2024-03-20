from flask_jwt_extended import decode_token

from app.model.repository.product import ProductRepository
from app.model.repository.type import TypeRepository
from app.model.repository.order import OrderRepository
from app.model.repository.plan import PlanRepository
from app.utils.errors.GException import GException
from app.utils.errors.UserNotFoundException import UserNotFoundException
from app.utils.utils import createSuccessResponse, createErrorResponse


class PlanService:

    @classmethod
    def getPlans(cls):
        plans = PlanRepository.getPlans()
        return createSuccessResponse([e.toJSON() for e in plans])