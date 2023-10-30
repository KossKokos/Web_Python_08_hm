
# import modules needed for connection and creating models
from mongoengine import connect
from mongoengine import Document
from mongoengine.fields import ListField, StringField, ReferenceField


# connection to the database
connect(host=f"""mongodb+srv://goitlearn:gNzmAJhyAtceMXpV@cluster.pdfljge.mongodb.net/homework_08?retryWrites=true&w=majority""", ssl=True)

# creating collection authors
class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

# creating collection qoutes
class Qoutes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Authors)
    qoute = StringField()