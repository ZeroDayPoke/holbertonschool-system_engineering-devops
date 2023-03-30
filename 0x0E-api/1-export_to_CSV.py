#!/usr/bin/python3
"""doc"""
import sys
import requests
import csv

def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    if 'name' not in user_data:
        print("Invalid employee ID")
        return None, None

    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos_data = todos_response.json()

    return user_data, todos_data

def export_to_csv(employee_id, user_data, todos_data):
    file_name = f"{employee_id}.csv"
    
    with open(file_name, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        for task in todos_data:
            csv_writer.writerow([employee_id, user_data["username"], task["completed"], task["title"]])

    print(f"Data exported to {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_data, todos_data = get_employee_data(employee_id)

    if user_data and todos_data:
        export_to_csv(employee_id, user_data, todos_data)