FROM python:3.10

WORKDIR /application_consumer

COPY ./application_consumer/routes /application_consumer/routes
COPY ./application_consumer/main.py /application_consumer/main.py
COPY ./requirements.txt /application_consumer/requirements.txt
COPY ./messages_broker.py /application_consumer/messages_broker.py

RUN pip install -r requirements.txt

# Запуск приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
