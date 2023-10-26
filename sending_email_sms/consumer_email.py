from bson import ObjectId
from importlib.machinery import SourceFileLoader
import sys
import pika
from pika.exchange_type import ExchangeType
sys.path.append(r'C:\Users\kosko\Documents\Python\Python_Web\Web_Python_hm_08\Web_Python_08_hm\sending_email')
from producer import Contacts


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='notification', exchange_type=ExchangeType.direct)

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(
        exchange='notification', queue=queue_name, routing_key='send_email')

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    id_ = ObjectId(body.decode())
    contacts = Contacts.objects(id=id_)
    for c in contacts:
        c.update(received_email = True)
    print(f"message was sent to email: {c.email}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name, on_message_callback=callback)

if __name__ == '__main__':
    channel.start_consuming()