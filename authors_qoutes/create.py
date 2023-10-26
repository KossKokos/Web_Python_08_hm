from models import Authors, Qoutes
import json

if __name__ == '__main__':
    # open files and read it using json module
    with open('authors.json', 'r', encoding='utf-8') as fh:
        authors_json = json.load(fh)

    with open('qoutes.json', 'r', encoding='utf-8') as file:
        qoutes_json = json.load(file)

    # first albert's description going to albert_json, steave's dict going to steave_json
    albert_json = authors_json[0]
    steave_json = authors_json[1]

    # creating an modules in authors
    albert = Authors(fullname=albert_json['fullname'], born_date=albert_json['born_date'],\
                    born_location=albert_json['born_location'],\
                    description=albert_json['description']).save()
    
    steave = Authors(fullname=steave_json['fullname'], born_date=steave_json['born_date'],\
                    born_location=steave_json['born_location'],\
                    description=steave_json['description']).save()

    # checking who is the author of the quote
    for qoute in qoutes_json:
        if qoute['author'] == 'Albert Einstein':
            quote_model = Qoutes(tags=qoute['tags'], author=albert, qoute=qoute['quote']).save()
        else:
            quote_model = Qoutes(tags=qoute['tags'], author=steave, qoute=qoute['quote']).save()

