from flask import Flask

from src.app.kenzie import is_a_valid_key, is_a_valid_values
from config import *

from src.middlewares import database
from src.blueprints.user_bp import bp as UserBlueprint

app = Flask(__name__)

# Mapping configuration sources
app.config.from_object(DevelopmentConfig())

# Registering blueprints
app.register_blueprint(UserBlueprint)

# Initial startup
app.before_first_request(database.run_migrations)
