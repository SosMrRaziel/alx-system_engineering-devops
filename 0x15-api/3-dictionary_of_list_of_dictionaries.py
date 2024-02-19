#!/usr/bin/python3

""" a Python script that, using this REST API"""

import json
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    # Create an empty dictionary to store the data
    data = {}

    # Loop through the user ids from 1 to 10
    for employee_id in range(1, 11):
        response = requests.get(base_url + "users/" + str(employee_id))
        employee_name = response.json()["username"]

        # Get the employee's TODO list from the API
        response = requests.get(base_url + "todos?userId=" + str(employee_id))
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

        # Update the data dictionary with the user id and the tasks
        data.update({employee_id: tasks})

    # Create a JSON file named todo_all_employees.json
    with open("todo_all_employees.json", "w") as jsonfile:
        # Write the data to the file with 4 spaces indentation
        json.dump(data, jsonfile)
