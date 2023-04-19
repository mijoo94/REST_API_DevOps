import requests

# Define the API URL
API_URL = "http://localhost:5000"

# Add an employee
print("Adding an employee...")
employee = {"name": "John Doe", "email": "john.doe@example.com", "department": "IT"}
response = requests.post(f"{API_URL}/employees", json=employee)
print(response.json())
print()

# Get all employees
print("Getting all employees...")
response = requests.get(f"{API_URL}/employees")
print(response.json())
print()

# Get the ID of the employee we just added
print("Getting the ID of the employee we just added...")
employees = response.json()
ID = employees[-1]['id']
print(f"ID: {ID}")
print()

# Update the employee we just added
print("Updating the employee we just added...")
updated_employee = {"name": "John Doe Jr.", "email": "john.doe.jr@example.com", "department": "Marketing"}
response = requests.put(f"{API_URL}/employees/{ID}", json=updated_employee)
print(response.json())
print()

# Get the updated employee
print("Getting the updated employee...")
response = requests.get(f"{API_URL}/employees/{ID}")
print(response.json())
print()

# Delete the employee
print("Deleting the employee...")
response = requests.delete(f"{API_URL}/employees/{ID}")
print(response.json())
print()

# Get all employees again to verify the employee was deleted
print("Getting all employees again...")
response = requests.get(f"{API_URL}/employees")
print(response.json())
print()
