from sqlalchemy import text
from sqlalchemy.sql.functions import random

from app.configuration.config import sql
from app.model.entity.order import Order
from app.model.entity.product import Product
from app.model.entity.review import Review
from app.utils.utils import generateUuid


class ReviewRepository:

    @classmethod
    def getReviews(cls):
        reviews = sql.session.query(Review).order_by(random()).limit(4).all()
        return reviews

    @classmethod
    def create(cls, userId, content, stars):
        review = Review(userId, content, stars)
        sql.session.add(review)
        sql.session.commit()
        return review