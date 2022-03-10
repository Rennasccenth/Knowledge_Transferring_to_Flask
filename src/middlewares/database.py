import os
from src.app.kenzie.system import create_database


def run_migrations():
    """
    Run database migrations
    :return: None
    """
    base_path = os.environ.get("DATABASE_PATH")
    create_database(path=base_path)
