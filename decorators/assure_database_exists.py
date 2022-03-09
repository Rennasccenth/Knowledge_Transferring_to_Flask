import os
from app.kenzie.system import mk_database


def assure_database_exists(function):
    @wrap(function)
    def wrap(*args, **kwargs):
        if not os.path.isdir("./app/database"):
            mk_database()
        return function(*args, **kwargs)

    return wrap
