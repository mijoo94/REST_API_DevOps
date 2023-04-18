import sqlite3

conn = sqlite3.connect('employee_management.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        department TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
 
