import pika
from pika.exchange_type import ExchangeType
from mongoengine import connect
from mongoengine import Document
from mongoengine.fields import StringField, BooleanField
from faker import Faker


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='send_email_ex', exchange_type=ExchangeType.direct)
channel.queue_declare(queue='send_email_qu', durable=True)
channel.queue_bind(exchange='send_email_ex', queue='send_email_qu')

connect(host=f"""mongodb+srv://goitlearn:gNzmAJhyAtceMXpV@cluster.pdfljge.mongodb.net/homework_08?retryWrites=true&w=majority""", ssl=True)

class Contacts(Document):
    fullname = StringField(max_length=300)
    email = StringField(max_length=300)
    phone = StringField(max_length=300)
    received_email = BooleanField(default=False)
    received_sms = BooleanField(default=False)

fake = Faker()

def main():
    for _ in range(5):
        contact = Contacts(fullname=fake.name(), email=fake.email()).save()

        channel.basic_publish(
            exchange='send_email_ex',
            routing_key='send_email_qu',
            body=str(contact.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(str(contact.id))
        print(f'Sent email to {contact.fullname}')
    connection.close()

if __name__ == '__main__':
    main()