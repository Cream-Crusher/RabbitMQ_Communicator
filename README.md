# RabbitMQ Communicator

Сервисы с API методами для реализации связи Publisher/Consumer через RabbitMQ

## Стэк
* Python 3.10
* fastapi 0.104.1
* RabbitMQ(aio-pik) 9.3.0 
* docker + docker-compose

## Запуск

### Clone repo
```git clone git@github.com:Cream-Crusher/RabbitMQ_Communicator.git```
### Run docker

  1. ```docker-compose up -d --build```
  2. ```docker-compose up```


### View Swagger
* Swagger с API методом: **Post**, для создания сообщения в очереди RabbitMQ: ```http://0.0.0.0:8000/docs#```
* Swagger с API методом: **Get**, для получение сообщения из очереди RabbitMQ ```http://0.0.0.0:8001/docs#```

## Особенности реализации

### Сервисы:
* **application_consumer**: Является независимым сервисом Consumer-ом для RabbitMQ.
* **application_publisher**: Является независимым сервисом Publisher-ом для RabbitMQ.
* **RabbitMQ**: Является брокером сообщений для других севрисов.

### REST-API:

* Сервис: **application_consumer**
  * [GET] **get_message** (routing_key: str) - Осуществялет запрос к очереди(Queue) использую ключ очереди(routing_key) для получения сообщения(Message)`. Возвращает ответ с телом сообщения.


* Сервис: **application_publisher**
  * [POST] **post_message** (routing_key: str, message: str) - Осуществялет передачу сообщения(Message) в очередь(Queue) RbbitMQ использую ключ очереди(routing_key), в результате чего создаётся отдельная очередь(Если она ещё не была создана ранее), куда записывается тело сообщения.


* Сервис: **RabbitMQ**
  * **MessageBrokerRabbitMQ** - Является классом-интерфейсом, включающий следующие компоненты(адаптеры):
    * **get_rabbitmq_connection** - Осуществялет подлкючение к хосу RabbitMQ.
    * **send_message** (message: str, routing_key: str) - Подключается к RabbitMQ и осуществялет передачу сообщения(Message) в очередь(Queue) RbbitMQ использую ключ очереди(routing_key), в результате чего создаётся отдельная очередь(Если она ещё не была создана ранее), куда записывается тело сообщения.
    * **get_massege** (routing_key: str) - Подключается к RabbitMQ и осуществялет запрос к очереди(Queue) использую ключ очереди(routing_key) для получения сообщения(Message)`. Возвращает ответ с телом сообщения.
