from sqlalchemy import text

from app.configuration.config import sql
from app.model.entity.order import Order
from app.utils.utils import generateUuid


class OrderRepository:

    @classmethod
    def getOrders(cls, user_id):
        products = sql.session.query(Order).filter(Order.user_id == user_id).all()
        return products

    @classmethod
    def getEarnings(cls, user_id):
        products = sql.session.query(text("earnings")).from_statement(
            text("SELECT SUM(p.cost) AS earnings "
                 "FROM orders o "
                 "JOIN products p "
                 "ON o.product_id = p.product_id "
                 "WHERE p.user_id = :user_id"
            ).params(user_id=user_id)
        ).first()
        return products

    @classmethod
    def getOrdersGraph(cls, type, user_id):

        tp = {
            'name': '',
            'value': ''
        }
        if type == "day":
            tp = {
                'name': 'hour',
                'where': 'DAY(orders.created_on) = DAY(CURRENT_DATE)',
                'value': "HOUR(orders.created_on) AS hour"
            }
        elif type == "week":
            tp = {
                'name': 'day',
                'where': 'WEEK(orders.created_on) = WEEK(CURRENT_DATE)',
                'value': "DAYOFWEEK(orders.created_on) AS day"
            }
        elif type == "month":
            tp = {
                'name': 'day',
                'where': 'MONTH(orders.created_on) = MONTH(CURRENT_DATE)',
                'value': "DAY(orders.created_on) AS day"
            }
        elif type == "year":
            tp = {
                'name': 'month',
                'where': 'YEAR(orders.created_on) = YEAR(CURRENT_DATE)',
                'value': "MONTH(orders.created_on) AS month"
            }

        products = sql.session.query(text("n"), text(tp.get("name"))).from_statement(
            text("SELECT COUNT(*) AS n, " + tp.get("value") + " "
                 "FROM orders "
                 "JOIN products p "
                 "ON orders.product_id = p.product_id "
                 "WHERE p.user_id = :user_id "
                 "AND " + tp.get("where") + " "
                 "GROUP BY " + tp.get("value").split(" ")[0]
            ).params(user_id=user_id)
        ).all()
        print(products)
        return products

    @classmethod
    def getEarningsGraph(cls, type, user_id):

        tp = {
            'name': '',
            'value': ''
        }
        if type == "day":
            tp = {
                'name': 'hour',
                'where': 'DAY(orders.created_on) = DAY(CURRENT_DATE)',
                'value': "HOUR(orders.created_on) AS hour"
            }
        elif type == "week":
            tp = {
                'name': 'day',
                'where': 'WEEK(orders.created_on) = WEEK(CURRENT_DATE)',
                'value': "DAYOFWEEK(orders.created_on) AS day"
            }
        elif type == "month":
            tp = {
                'name': 'day',
                'where': 'MONTH(orders.created_on) = MONTH(CURRENT_DATE)',
                'value': "DAY(orders.created_on) AS day"
            }
        elif type == "year":
            tp = {
                'name': 'month',
                'where': 'YEAR(orders.created_on) = YEAR(CURRENT_DATE)',
                'value': "MONTH(orders.created_on) AS month"
            }

        products = sql.session.query(text("n"), text(tp.get("name"))).from_statement(
            text("SELECT SUM(p.cost) AS n, " + tp.get("value") + " "
                 "FROM orders "
                 "JOIN products p "
                 "ON orders.product_id = p.product_id "
                 "WHERE p.user_id = :user_id "
                 "AND " + tp.get("where") + " "
                 "GROUP BY " + tp.get("value").split(" ")[0]
            ).params(user_id=user_id)
        ).all()
        print(products)
        return products

    @classmethod
    def create(cls, user_id, productId):
        order = Order(user_id, productId)
        sql.session.add(order)
        sql.session.commit()
        return order

    @classmethod
    def getOrder(cls, user_id, productId):
        order = sql.session.query(Order).filter(Order.user_id == user_id, Order.product_id == productId).first()
        return order

    @classmethod
    def getOrderByTk(cls, param):
        order = sql.session.query(Order).filter(Order.tk == param).first()
        order.tk = None
        sql.session.commit()
        return order