#!/usr/bin/python3

""" a Python script that, using this REST API"""

import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    response = requests.get(base_url + "users/" + employee_id)
    employee_name = response.json()["username"]

    # Get the employee's TODO list from the API
    response = requests.get(base_url + "todos?userId=" + employee_id)
    todo_list = response.json()

    # Create a list of dictionaries to store the tasks
    tasks = []

    # Loop through the TODO list
    for task in todo_list:
        # Create a dictionary for each task
        task_dict = {}
        # Store the relevant information in the dictionary
        task_dict["task"] = task["title"]
        task_dict["completed"] = task["completed"]
        task_dict["username"] = employee_name
        # Append the dictionary to the list
        tasks.append(task_dict)

    # Create a dictionary with the user id as the key & the tasks as the value
    data = {employee_id: tasks}

    # Create a JSON file named USER_ID.json
    with open(employee_id + ".json", "w") as jsonfile:
        # Write the data to the file with 4 spaces indentation
        json.dump(data, jsonfile)
