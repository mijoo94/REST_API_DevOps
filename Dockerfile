FROM ubuntu 

RUN apt-get update -y
RUN apt-get install python3-pip -y

FROM python:3.9-slim-buster
RUN pip install Flask

ADD app.py /
WORKDIR /

EXPOSE 5000

COPY . .

# Check if the database file exists before running the program
RUN test -f /employee_management.db

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
