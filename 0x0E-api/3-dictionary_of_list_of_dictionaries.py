#!/usr/bin/python3
"""doc"""
import requests
import json

def get_all_employees():
    base_url = "https://jsonplaceholder.typicode.com"
    
    user_response = requests.get(f"{base_url}/users")
    user_data = user_response.json()

    return user_data

def get_employee_tasks(user_id, username):
    base_url = "https://jsonplaceholder.typicode.com"
    
    todos_response = requests.get(f"{base_url}/users/{user_id}/todos")
    todos_data = todos_response.json()

    task_data = []
    for task in todos_data:
        task_data.append({
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
        })

    return task_data

def export_to_json(all_employees_data):
    file_name = "todo_all_employees.json"
    
    all_tasks = {}
    for employee in all_employees_data:
        user_id = employee["id"]
        username = employee["username"]
        tasks = get_employee_tasks(user_id, username)
        all_tasks[user_id] = tasks

    with open(file_name, "w") as jsonfile:
        json.dump(all_tasks, jsonfile)

    print(f"Data exported to {file_name}")

if __name__ == "__main__":
    all_employees_data = get_all_employees()
    export_to_json(all_employees_data)
