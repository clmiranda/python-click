import json
import os


def read_json():
    if not os.path.isfile("data.json"):
        with open("data.json", "w") as file:
            json.dump([], file)

    with open("data.json", "r") as file:
        users = json.load(file)

    return users


def search_name_repeated(name):
    users = read_json()
    result = len([user for user in users if user["name"].lower() == name.lower()])
    return result


def write_json(data):
    with open("data.json", "w") as file:
        json.dump(data, file)
