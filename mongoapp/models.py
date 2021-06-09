from django.db import models

from mongoengine import Document, fields, DynamicDocument, EmbeddedDocument
from datetime import datetime
from mongoengine import connect, disconnect
connect('mydb')

class Tag(Document):
    customer_id = fields.StringField()
    tag_cus = fields.ListField(fields.StringField(max_length=40))
