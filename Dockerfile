FROM python:3.9-slim
RUN apt-get clean && apt-get -y update
RUN apt-get -y install nginx python3-dev build-essential

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt --src /usr/local/src

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

COPY . .
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]