from json import dump
import os


def mk_database():
    json = {"data": []}
    os.mkdir("./app/database")
    with open("./app/database/database.json", "w") as json_file:
        dump(json, json_file, indent=4)
