from mongoengine import Document, StringField, IntField

class Item(Document):
    name = StringField(required=True)
    quantity = IntField(default=0)

    meta = {
        'collection': 'food'
    }