from json import dump
import os


def mk_database():
    print("Creating database...")

    empty_json_data = {"data": []}
    base_path: str = os.environ.get("DATABASE_PATH")

    # Creating folder
    os.mkdir(base_path)

    # Creating json file
    full_path = base_path + "/database.json"
    with open(full_path, "w+") as json_file:
        dump(empty_json_data, json_file, indent=4)

    print(f"Database created at {full_path}...")
