#!/usr/bin/python3
"""a Python script that, using jsonplaceholder.typicode REST API,
for a given employee ID, returns information about his/her
TODO list progress and  export data in the CSV format."""
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    user_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(emp_id)).json().get("username")
    task_status = []
    task_title = []

    request = requests.get('https://jsonplaceholder.typicode.com//todos')\
        .json()

    for test in request:
        if test.get('userId') == int(emp_id):
            task_status.append(test.get('completed'))
            task_title.append(test.get('title'))
    with open("{}.csv".format(emp_id), "a") as f:
        for status, title in zip(task_status, task_title):
            print('"{}","{}","{}","{}"'
                  .format(emp_id, user_name, status, title), file=f)
