from app.configuration.config import sql


class Plan(sql.Model):
    __tablename__ = "plans"
    plan_id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(14), nullable=False)
    cost = sql.Column(sql.Integer, nullable=False)
    premium = sql.Column(sql.Boolean, nullable=False)
    favorite = sql.Column(sql.Boolean, nullable=False)
    points = sql.Column(sql.String(150), nullable=False)

    def __init__(self, name, premium, favorite, cost, points):
        self.name = name
        self.favorite = favorite
        self.premium = premium
        self.cost = cost
        self.points = points

    def toJSON(self, **kvargs):
        obj = {
            'plan_id': self.plan_id,
            'name': self.name,
            'premium': self.premium,
            'favorite': self.favorite,
            'cost': self.cost,
            'points': self.points
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj