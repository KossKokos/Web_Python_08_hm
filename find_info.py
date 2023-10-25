from pprint import pprint

import redis
from redis_lru import RedisLRU

from models import Authors, Qoutes

client = redis.StrictRedis(host="localhost", port=6379, username='default', password=None)
cache = RedisLRU(client)

# func gets author's info using fullname from mongodb
@cache
def authors_name(args):
    fullname = args.strip()
    authors = Authors.objects(fullname__icontains=fullname) # icontains mean insensitive case and contains(like regex)
    for author in authors:
        pprint(f'fullname: {author.fullname}, born date: {author.born_date}, born location: {author.born_location}\
            description: {author.description}')
        print('*'*80)

# func gets author's info using born date from mongodb
def authors_b_date(args):
    b_date = args.strip()
    authors = Authors.objects(born_date__icontains=b_date)
    for author in authors:
        pprint(f'fullname: {author.fullname}\
                born date: {author.born_date}\
                born location: {author.born_location}\
                description: {author.description}') 
        print('*'*80)

# func gets author's info using born location from mongodb
def authors_location(args):
    location = args.strip()
    authors = Authors.objects(born_location__icontains=location)
    for author in authors:
        pprint(f'fullname: {author.fullname}\
                born date: {author.born_date}\
                born location: {author.born_location}\
                description: {author.description}')
        print('*'*80)

# func gets author's info using description from mongodb
def authors_description(args):
    description = args.strip()
    authors = Authors.objects(description__icontains=description)
    for author in authors:
        pprint(f'fullname: {author.fullname}\
                born date: {author.born_date}\
                born location: {author.born_location}\
                description: {author.description}') 
        print('*'*80)

# func gets qoute's info using tag from mongodb
@cache
def qoutes_tag(args):
    tag = args.strip()
    qoutes = Qoutes.objects(tags__icontains=tag)# single tag
    for qoute in qoutes:
        pprint(f'tags: {qoute.tags}, author: {qoute.author.fullname}, qoute: {qoute.qoute}')
        print('*'*80)

# func gets qoute's info using tags from mongodb
def qoutes_tags(args):
    tags = args.strip().split(',')
    qoutes = Qoutes.objects(tags__in__icontains=tags)# list of tags
    for qoute in qoutes:
        pprint(f'tags: {qoute.tags}, author: {qoute.author.fullname}, qoute: {qoute.qoute}')
        print('*'*80)

# func gets qoute's info using qoute from mongodb
def qoutes_qoute(args):
    qoute = args.strip()
    qoutes = Qoutes.objects(qoute__icontains=qoute)
    for qoute in qoutes:        
        pprint(f'tags: {qoute.tags}, author: {qoute.author.fullname}, qoute: {qoute.qoute}')
        print('*'*80)

# dict, where keys are commands(user input) and values are funcs
commands = {'name': authors_name, 'date': authors_b_date, 'location': authors_location,
                'description': authors_description, 'tag': qoutes_tag, 'tags': qoutes_tags,
                'qoute': qoutes_qoute}

def main():
    # loop is working untill user enter exit command
    while True:
        try:
            user_input = input('>>> ').strip() 
            if user_input.lower() == 'exit':
                print('Bye')
                break
            comm, args = user_input.split(':') # parse user_input
            commands.get(comm)(args) # calling a function using a key
        except TypeError:
            print('Wrong command')
        except ValueError:
            print('Not enough params')

if __name__ == '__main__':
    main()