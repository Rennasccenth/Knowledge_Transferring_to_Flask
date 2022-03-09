import os
from http import HTTPStatus
from json import load

from flask import Blueprint

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.get("")
def get_all_users():
    base_path = os.environ.get("DATABASE_PATH")
    with open(base_path + "/database.json", "r") as json_file:
        return load(json_file), HTTPStatus.OK

# @bp.post("")
# def post_user():
#     body: dict = request.get_json()
#
#     if not is_a_valid_key(body):
#         return {"error": "wrong key"}, HTTPStatus.BAD_REQUEST
#
#     if not is_a_valid_values(body):
#         pt = type(123.23)
#         print(pt.__qualname__)
#         # return {
#         #             "wrong fields": [
#         #                 {
#         #                     "nome": str(type(body["nome"]))
#         #                 },
#         #                 {
#         #                     "email": str(type(body["email"]))
#         #                 }
#         #             ]
#         #         }, HTTPStatus.BAD_REQUEST
#
#     return ""
