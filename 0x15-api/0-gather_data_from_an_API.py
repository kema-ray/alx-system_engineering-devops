#!/usr/bin/python3
"""
Python script that uses REST API, for a given employee ID, returns
information about his/her TODO list progress
"""
import requests
import sys


API = "https://jsonplaceholder.typicode.com/"
"""
REST API url
"""


if __name__ == '__main__':
    user = requests.get(API + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(API + "todos", params={"userId": sys.argv[1]}).json()

    completed = [todo.get("title")
    for todo in todos 
    if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(complete)) for complete in completed]
