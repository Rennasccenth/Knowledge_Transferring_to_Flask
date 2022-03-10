import json
import os
from http import HTTPStatus
from json import dumps

from flask import Blueprint, request

from src.services.user_service_impl import UserService, UserServiceImpl

bp = Blueprint("user", __name__, url_prefix="/user")


# HTTP Request -> (APP Flask(server) -----> Router ----- Blueprint --> Processamento -> Devolve
# resultado) -> HTTP Response
@bp.get("")
def get_all_users():
    # TODO: Se usássemos Injeção de Dependência, nós nunca iríamos ficar instanciando as
    #  Implementações ao longo do código, e sim só as abstrações
    user_service = UserServiceImpl()
    all_users = user_service.get_all()

    if all_users:
        # TODO: Ele vai reclamar sobre não conseguir serializar o objeto [User]
        #  sugiro dar uma olhada no pydantic
        return dumps(all_users), HTTPStatus.OK
    else:
        return dumps(list()), HTTPStatus.NO_CONTENT

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
