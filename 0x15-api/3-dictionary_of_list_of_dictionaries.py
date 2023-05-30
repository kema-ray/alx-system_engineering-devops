#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""
import json
import requests

api = "https://jsonplaceholder.typicode.com/"
"""
REST API url
"""

if __name__ == "__main__":
    users = requests.get(api + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            } for todo in requests.get(api + "todos",params={"userId": user.get("id")}).json()]
            for user in users}, jsonfile)
