from http import HTTPStatus
from json import dump, load
import os
from flask import Flask, request
from app.kenzie import mk_database, is_a_valid_key, is_a_valid_values
from blueprints import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)


@app.post("/user")
def post_user():
    body: dict = request.get_json()

    if not os.path.isdir("./app/database"):
        mk_database()

    if not is_a_valid_key(body):
        return {"error": "wrong key"}, HTTPStatus.BAD_REQUEST

    if not is_a_valid_values(body):
        pt = type(123.23)
        print(pt.__qualname__)
        # return {
        #             "wrong fields": [
        #                 {
        #                     "nome": str(type(body["nome"]))
        #                 },
        #                 {
        #                     "email": str(type(body["email"]))
        #                 }
        #             ]
        #         }, HTTPStatus.BAD_REQUEST

    return ""
