#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"


    response = requests.get(base_url + "users/" + employee_id)
    employee_name = response.json()["name"]

    # Get the employee's TODO list from the API
    response = requests.get(base_url + "todos?userId=" + employee_id)
    todo_list = response.json()

    # Count the number of completed and total tasks
    completed_tasks = 0
    total_tasks = len(todo_list)

    # Store the titles of completed tasks in a list
    completed_titles = []

    # Loop through the TODO list
    for task in todo_list:
        # If the task is completed, increment the counter and append the title
        if task["completed"]:
            completed_tasks += 1
            completed_titles.append(task["title"])

    # Print the employee's TODO list progress
    print("Employee {} is done with tasks({}/{})".format(
                                                            employee_name,
                                                            completed_tasks,
                                                            total_tasks))

    for title in completed_titles:
        print("\t " + title)
