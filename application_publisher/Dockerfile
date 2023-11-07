FROM python:3.10

WORKDIR /application_publisher

COPY ./routes /application_publisher/routes
COPY ./main.py /application_publisher/main.py
COPY ./message_broker.py /application_publisher/message_broker.py
COPY requirements.txt /application_publisher/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

# Запуск приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
