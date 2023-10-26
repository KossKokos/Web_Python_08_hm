import random
import sys

import pika
from pika.exchange_type import ExchangeType
from faker import Faker
sys.path.append(r'C:\Users\kosko\Documents\Python\Python_Web\Web_Python_hm_08\Web_Python_08_hm\sending_email')
from producer import Contacts

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='notification', exchange_type=ExchangeType.direct)

email_sms = ['send_email', 'send_sms']

fake = Faker()

def main():
    for _ in range(10):
        contact = Contacts(fullname=fake.name(), email=fake.email(), phone=fake.phone_number()).save()

        channel.basic_publish(
            exchange='notification',
            routing_key=random.choice(email_sms),
            body=str(contact.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(str(contact.id))
        print(f'Sent email to {contact.fullname}')
    connection.close()

if __name__ == '__main__':
    main()