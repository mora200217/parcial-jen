# mypage/models.py
from mongoengine import Document, StringField, FloatField, IntField, BooleanField, DateTimeField

class Food(Document):
    name = StringField(required=True, max_length=100)         # Name of the food
    description = StringField(max_length=500)                # Optional description
    price = FloatField(required=True, min_value=0)           # Price in dollars or local currency
    calories = IntField(min_value=0)                          # Number of calories
    available = BooleanField(default=True)                   # Is it available for sale
    created_at = DateTimeField()                              # Creation date/time

    def __str__(self):
        return f"{self.name} - ${self.price}"
