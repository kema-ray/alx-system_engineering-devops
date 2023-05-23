#!/usr/bin/python3
"""
Script to export data in the CSV format
"""
import csv
import requests
import sys


api = "https://jsonplaceholder.typicode.com/"
"""
REST API url
"""


if __name__ == '__main__':
    user_id = sys.argv[1]
    user = requests.get(api + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(api + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, todo.get("completed"), todo.get("title")]
         ) for todo in todos]
