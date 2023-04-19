 
#!/bin/bash

# Define the API URL
API_URL="http:localhost:5000"

# Add an employee
echo "Adding an employee..."
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com", "department": "IT"}' $API_URL/employees
echo ""

# Get all employees
echo "Getting all employees..."
curl -X GET $API_URL/employees
echo ""

# Get the ID of the employee we just added
echo "Getting the ID of the employee we just added..."
ID=$(curl -X GET $API_URL/employees | jq -r '.[-1].id')
echo "ID: $ID"
echo ""

# Update the employee we just added
echo "Updating the employee we just added..."
curl -X PUT -H "Content-Type: application/json" -d '{"name": "John Doe Jr.", "email": "john.doe.jr@example.com", "department": "Marketing"}' $API_URL/employees/$ID
echo ""

# Get the updated employee
echo "Getting the updated employee..."
curl -X GET $API_URL/employees/$ID
echo ""

# Delete the employee
echo "Deleting the employee..."
curl -X DELETE $API_URL/employees/$ID
echo ""

# Get all employees again to verify the employee was deleted
echo "Getting all employees again..."
curl -X GET $API_URL/employees
echo ""
