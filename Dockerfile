FROM python:3.9-slim-buster

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Check if the database file exists before running the program
RUN test -f /app/employee_management.db

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
