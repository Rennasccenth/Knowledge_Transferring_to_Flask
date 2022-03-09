from http import HTTPStatus
from json import load
from flask import Blueprint

from decorators.assure_database_exists import assure_database_exists

user_bp = Blueprint("user", __name__, url_prefix="/user")


@assure_database_exists
def __on_first_request():
    return None


@user_bp.get()
def get_all_users():
    with open("./app/database/database.json", "r") as json_file:
        return load(json_file), HTTPStatus.OK


user_bp.before_app_first_request(__on_first_request)
