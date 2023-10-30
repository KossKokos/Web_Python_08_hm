from bson import ObjectId

import pika

from producer import Contacts


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='send_email_qu', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    id_ = ObjectId(body.decode())
    contacts = Contacts.objects(id=id_)
    for c in contacts:
        c.update(received = True)
    print(f"message was sent to email: {c.email}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='send_email_qu', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()