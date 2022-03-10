import os.path
from json import dump
from pathlib import Path


def create_database(path: str):
    """
    Run first migration
    :param path: Base path to start the database
    :return: Nothing
    """
    full_path = path + "/database.json"

    empty_json_data = {"data": []}

    file_not_exists = not os.path.exists(full_path)

    if file_not_exists:
        print("Creating database...")
        # Generating nested directories
        Path(path).mkdir(parents=True, exist_ok=True)

        # Creating json file
        with open(full_path, "w+") as json_file:
            dump(empty_json_data, json_file, indent=4)
        print(f"Database created at {full_path}...")
