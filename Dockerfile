FROM python:3.9-slim-buster

# WORKDIR = app
WORKDIR /app
# Copy project files into app directory
COPY . /app
# Install requirements
RUN pip install --no-cache-dir -r requirements.txt
#Listen to port 5000
EXPOSE 5000
# Check if the database file exists before running the program
RUN test -f /app/employee_management.db
#run the rest-api app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
