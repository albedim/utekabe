import datetime

from sqlalchemy import String, Column, Date, Boolean, DateTime
from app.configuration.config import sql
from app.utils.utils import generateUuid, BASE_URL, generateId, BASE_FE_URL


class User(sql.Model):
    __tablename__ = "users"
    user_id = sql.Column(sql.BigInteger, primary_key=True)
    email = sql.Column(sql.String(64), nullable=False)
    name = sql.Column(sql.String(24), nullable=False)
    surname = sql.Column(sql.String(24), nullable=False)
    bio = sql.Column(sql.String(200))
    recovery_token = sql.Column(sql.String(16))
    city = sql.Column(sql.String(14), nullable=False)
    plan_id = sql.Column(sql.Integer, sql.ForeignKey('plans.plan_id'), nullable=False)
    country_code = sql.Column(sql.String(4), nullable=False)
    paypal_email = sql.Column(sql.String(64), nullable=False)
    image_path = sql.Column(sql.Text, nullable=False)
    password = sql.Column(sql.String(64), nullable=False)
    library_name = sql.Column(sql.String(24), nullable=False)
    created_on = sql.Column(sql.Date, nullable=False)

    def __init__(self, email, name, surname, bio, imagePath, password, libraryName, city, country_code, paypal_email):
        self.user_id = generateId()
        self.email = email
        self.name = name
        self.surname = surname
        self.password = password
        self.bio = bio
        self.country_code = country_code
        self.city = city
        self.plan_id = 1
        self.paypal_email = paypal_email
        self.created_on = datetime.datetime.now()
        self.image_path = imagePath
        self.library_name = libraryName

    def toJSON(self, **kvargs):
        obj = {
            'user_id': self.user_id,
            'email': self.email,
            'name': self.name,
            'surname': self.surname,
            'bio': self.bio,
            'city': self.city,
            'country_code': self.country_code,
            'plan_id': self.plan_id,
            'paypal_email': self.paypal_email,
            'url': f"{BASE_FE_URL}/me/{self.library_name}",
            'image_path': f"{BASE_URL}/users/{self.user_id}/image",
            'library_name': self.library_name,
            'created_on': self.created_on.strftime("%Y-%m-%d")
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj