
# import modules needed for connection and creating models
from mongoengine import connect
from mongoengine import Document
from mongoengine.fields import ListField, StringField, ReferenceField


# connection to the database
connect(host=f"""mongodb+srv://goitlearn:gNzmAJhyAtceMXpV@cluster.pdfljge.mongodb.net/homework_08?retryWrites=true&w=majority""", ssl=True)

# creating collection authors
class Authors(Document):
    fullname = StringField(max_length=100, required=True)
    born_date = StringField(max_length=100)
    born_location = StringField(max_length=100)
    description = StringField()

# creating collection qoutes
class Qoutes(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Authors)
    qoute = StringField(max_length=300)