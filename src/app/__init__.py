from flask import Flask

from src.app.kenzie import is_a_valid_key, is_a_valid_values
from src.middlewares import database
from src.blueprints.user_bp import bp as UserBlueprint

app = Flask(__name__)
# TODO: Add configurações decentes nessa merda de flask ()
app.config.from_object("config.DevelopmentConfig")

app.register_blueprint(UserBlueprint)

app.before_first_request(database.initialize)
