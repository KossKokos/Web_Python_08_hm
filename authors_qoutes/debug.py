from models import Authors, Qoutes
import json

if __name__ == '__main__':
    # open files and read it using json module
    with open('authors_qoutes/authors.json', 'r', encoding='utf-8') as fh:
        authors_json = json.load(fh)

    with open('authors_qoutes/quotes.json', 'r', encoding='utf-8') as file:
        qoutes_json = json.load(file)

    for author_j in authors_json:
        author = Authors(fullname=author_j['fullname'], born_date=author_j['born_date'],\
                    born_location=author_j['born_location'],\
                    description=author_j['description']).save()
    for quote_j in qoutes_json:
        if quote_j['author'] == 'Alexandre Dumas fils':
            author = Authors.objects(fullname='Alexandre Dumas-fils')
            quote = Qoutes(tags=quote_j['tags'], author=author[0], qoute=quote_j['quote']).save()
            continue
        author = Authors.objects(fullname=quote_j['author'])
        quote = Qoutes(tags=quote_j['tags'], author=author[0], qoute=quote_j['quote']).save()

