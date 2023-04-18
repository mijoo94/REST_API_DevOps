import unittest
import requests

class TestEmployeeAPI(unittest.TestCase):
    BASE_URL = 'http://127.0.0.1:5000/employees'

    def test_get_all_employees(self):
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        employees = response.json()
        self.assertIsInstance(employees, list)
        for employee in employees:
            self.assertDictContainsSubset({'id': int, 'name': str, 'email': str, 'department': str}, employee)

    def test_get_employee(self):
        response = requests.get(f'{self.BASE_URL}/1')
        self.assertEqual(response.status_code, 200)
        employee = response.json()
        self.assertDictContainsSubset({'id': 1, 'name': str, 'email': str, 'department': str}, employee)

    def test_get_nonexistent_employee(self):
        response = requests.get(f'{self.BASE_URL}/999')
        self.assertEqual(response.status_code, 404)
        error = response.json()
        self.assertDictEqual(error, {'error': 'Employee not found'})

    def test_create_employee(self):
        employee_data = {'name': 'John Doe', 'email': 'johndoe@example.com', 'department': 'Sales'}
        response = requests.post(self.BASE_URL, json=employee_data)
        self.assertEqual(response.status_code, 201)
        employee = response.json()
        self.assertDictContainsSubset(employee_data, employee)
        self.assertIsInstance(employee['id'], int)

    def test_update_employee(self):
        employee_data = {'name': 'Jane Smith', 'email': 'janesmith@example.com', 'department': 'Marketing'}
        response = requests.put(f'{self.BASE_URL}/1', json=employee_data)
        self.assertEqual(response.status_code, 200)
        employee = response.json()
        self.assertDictContainsSubset(employee_data, employee)
        self.assertEqual(employee['id'], 1)

    def test_update_nonexistent_employee(self):
        employee_data = {'name': 'Jane Smith', 'email': 'janesmith@example.com', 'department': 'Marketing'}
        response = requests.put(f'{self.BASE_URL}/999', json=employee_data)
        self.assertEqual(response.status_code, 404)
        error = response.json()
        self.assertDictEqual(error, {'error': 'Employee not found'})

    def test_delete_employee(self):
        response = requests.delete(f'{self.BASE_URL}/1')
        self.assertEqual(response.status_code, 200)
        message = response.json()
        self.assertEqual(message, {'message': 'Employee deleted successfully'})

    def test_delete_nonexistent_employee(self):
        response = requests.delete(f'{self.BASE_URL}/999')
        self.assertEqual(response.status_code, 404)
        error = response.json()
        self.assertDictEqual(error, {'error': 'Employee not found'})

if __name__ == '__main__':
    unittest.main()
