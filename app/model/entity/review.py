import datetime

from app.configuration.config import sql
from app.utils.utils import generateUuid


class Review(sql.Model):
    __tablename__ = "reviews"
    review_id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    user_id = sql.Column(sql.BigInteger, sql.ForeignKey("users.user_id"), nullable=False)
    content = sql.Column(sql.String(200), nullable=False)
    created_on = sql.Column(sql.DateTime, nullable=False)
    stars = sql.Column(sql.Integer, nullable=False)

    def __init__(self, userId, content, stars):
        self.user_id = userId
        self.content = content
        self.stars = stars
        self.created_on = datetime.datetime.now()

    def toJSON(self, **kvargs):
        obj = {
            'review_id': self.review_id,
            'user_id': self.user_id,
            'content': self.content,
            'stars': self.stars,
            'created_on': self.created_on.strftime("%Y-%m-%d")
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj