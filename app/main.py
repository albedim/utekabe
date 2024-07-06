from flask import jsonify
from flask_cors import CORS

from app.configuration.config import sql, app
from app.routers import user, plan, product, order, review
from app.routers import type
from app.utils.utils import BASE_URL

app.register_blueprint(user.userRouter)
app.register_blueprint(product.productRouter)
app.register_blueprint(type.typeRouter)
app.register_blueprint(review.reviewRouter)
app.register_blueprint(plan.planRouter)
app.register_blueprint(order.orderRouter)

CORS(app)


@app.route("/")
def read_root():
    return jsonify({'documentation': f"{BASE_URL}/docs"})


def create_app():
    with app.app_context():
        sql.create_all()
    return app



if __name__ == "__main__":
    create_app().run(port=8000)
