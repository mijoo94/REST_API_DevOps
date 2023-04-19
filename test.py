import unittest
import requests

baseURL = 'http://127.0.0.1:5000/employees'
employee_id:str = ""
class TestAPI(unittest.TestCase):
    #add one employee
    def test_requests(self):
        data = {
            'name': 'majd',
            'email': 'majd@hotmail.com',
            'department': 'IT'
        }
        response = requests.post(baseURL, json=data)
        employee_id =response.json()['id']
        self.assertEqual(response.status_code, 201)
        
    #get the added employee  
        getURL = baseURL + "/" + str(employee_id)
        response = requests.get(getURL)
        self.assertEqual(response.status_code, 200)
        
    #delete the added employee  
        deleteURL = baseURL + "/" + str(employee_id)
        response = requests.delete(deleteURL)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
