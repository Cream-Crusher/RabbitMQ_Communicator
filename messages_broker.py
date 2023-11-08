from aio_pika import connect, Message


class MessageBrokerRabbitMQ:

    async def get_rabbitmq_connection(self):  # Подключение к серверу rabbitMQ
        connection = await connect(host='localhost')
        return connection

    async def send_message(self, message: str, routing_key: str):  # Отправка сообщения в очередь
        connection = await self.get_rabbitmq_connection()
        channel = await connection.channel()
        await channel.default_exchange.publish(
            Message(message.encode()),
            routing_key=routing_key  # Имя очереди
        )
        await connection.close()

    async def get_massege(self, routing_key: str):  # Получение сообщение из очереди кролика
        connection = await self.get_rabbitmq_connection()
        channel = await connection.channel()
        queue = await channel.declare_queue(routing_key)  # Имя очереди(routing_key)
        message = await queue.get(timeout=5, fail=False)
        if message:  # Сообщение обработанно и удалено из очереди
            await message.ack()
            message = message.body.decode()  # Обрабатываю сообщение

        await channel.close()  # закрытие канала
        await connection.close()  # закрытие соединения

        return message
