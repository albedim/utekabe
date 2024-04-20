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

    @classmethod
    def changePlan(cls, user, plan_id):
        user.plan_id = plan_id
        sql.session.commit()
        return user

    @classmethod
    def getPlanById(cls, param):
        plan = sql.session.query(Plan).filter(Plan.plan_id == param).first()
        return plan