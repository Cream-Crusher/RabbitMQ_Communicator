from aio_pika import connect, Message


async def get_rabbitmq_connection():  # Подключение к серверу rabbitMQ
    connection = await connect(host='localhost')
    return connection


async def send_message(message, routing_key):  # Отправка сообщения в очередь
    connection = await get_rabbitmq_connection()
    channel = await connection.channel()
    await channel.default_exchange.publish(
        Message(message.encode()),
        routing_key=routing_key  # Имя очереди
    )
    await connection.close()
