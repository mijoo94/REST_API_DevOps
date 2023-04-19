FROM python:3.9-slim-buster

RUN apt-get install libsqlite3-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Check if the database file exists before running the program
RUN test -f /app/employee_management.db

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
