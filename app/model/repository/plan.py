from sqlalchemy import text

from app.configuration.config import sql
from app.model.entity.plan import Plan
from app.model.entity.user import User


class PlanRepository:

    @classmethod
    def getPlans(cls):
        plans = sql.session.query(Plan).all()
        return plans

    @classmethod
    def getPlan(cls, userId):
        plan = sql.session.query(Plan).join(User, User.plan_id == Plan.plan_id).filter(User.user_id == userId).first()
        return plan