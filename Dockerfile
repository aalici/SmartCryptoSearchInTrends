FROM python:3.8-slim-buster

WORKDIR /app
COPY . .

RUN apt-get update
RUN apt-get install -y git

RUN pip install -r requirements.txt

CMD ["python","src/schedule.py"]
