from flask import Flask, request, jsonify
import sqlite3
#test test test test
app = Flask(__name__)

@app.route('/employees', methods=['GET'])
def get_employees():
    conn = sqlite3.connect('employee_management.db')
    c = conn.cursor()
    c.execute('SELECT * FROM employees')
    employees = c.fetchall()
    conn.close()
    response = jsonify([{'id': e[0], 'name': e[1], 'email': e[2], 'department': e[3]} for e in employees])
    return response, 200 

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    conn = sqlite3.connect('employee_management.db')
    c = conn.cursor()
    c.execute('SELECT * FROM employees WHERE id=?', (id,))
    employee = c.fetchone()
    conn.close()
    if employee:
        return jsonify({'id': employee[0], 'name': employee[1], 'email': employee[2], 'department': employee[3]})
    else:
        return jsonify({'error': 'Employee not found'}), 404

@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.json
    conn = sqlite3.connect('employee_management.db')
    c = conn.cursor()
    c.execute('INSERT INTO employees (name, email, department) VALUES (?, ?, ?)', (data['name'], data['email'], data['department']))
    conn.commit()
    employee_id = c.lastrowid
    conn.close()
    return jsonify({'id': employee_id, 'name': data['name'], 'email': data['email'], 'department': data['department']}), 201

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    conn = sqlite3.connect('employee_management.db')
    c = conn.cursor()
    c.execute('SELECT * FROM employees WHERE id=?', (id,))
    employee = c.fetchone()
    if not employee:
        conn.close()
        return jsonify({'error': 'Employee not found'}), 404
    data = request.json
    c.execute('UPDATE employees SET name=?, email=?, department=? WHERE id=?', (data['name'], data['email'], data['department'], id))
    conn.commit()
    conn.close()
    return jsonify({'id': id, 'name': data['name'], 'email': data['email'], 'department': data['department']})

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    conn = sqlite3.connect('employee_management.db')
    c = conn.cursor()
    c.execute('SELECT * FROM employees WHERE id=?', (id,))
    employee = c.fetchone()
    if not employee:
        conn.close()
        return jsonify({'error': 'Employee not found'}), 404
    c.execute('DELETE FROM employees WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Employee deleted successfully'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
