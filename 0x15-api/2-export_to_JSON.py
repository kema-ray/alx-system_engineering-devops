#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    api = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(api + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            } for todo in todos]}, jsonfile)
