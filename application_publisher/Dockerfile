FROM python:3.10

WORKDIR /application_publisher

COPY ./application_publisher/routes /application_publisher/routes
COPY ./application_publisher/main.py /application_publisher/main.py
COPY ./requirements.txt /application_publisher/requirements.txt
COPY ./messages_broker.py /application_publisher/messages_broker.py

RUN pip install -r requirements.txt

EXPOSE 8000

# Запуск приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
