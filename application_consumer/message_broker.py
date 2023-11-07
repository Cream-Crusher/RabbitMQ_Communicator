from aio_pika import connect


async def get_rabbitmq_connection():  # Подключение к серверу rabbitMQ
    connection = await connect(host='localhost')
    return connection


async def get_massege(routing_key):  # Получение сообщение из очереди кролика
    connection = await get_rabbitmq_connection()
    channel = await connection.channel()
    queue = await channel.declare_queue(routing_key)  # Имя очереди(routing_key)
    message = await queue.get(timeout=5, fail=False)
    if message:  # Сообщение обработанно и удалено из очереди
        await message.ack()

    await channel.close()  # закрытие канала
    await connection.close()  # закрытие соединения

    return message
