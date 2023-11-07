FROM python:3.10

WORKDIR /application_consumer

COPY ./routes /application_consumer/routes
COPY ./main.py /application_consumer/main.py
COPY ./message_broker.py /application_consumer/message_broker.py
COPY requirements.txt /application_consumer/requirements.txt

RUN pip install -r requirements.txt

# Запуск приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
