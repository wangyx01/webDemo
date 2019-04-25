import json
from os import path

from django.db import models
from django.db.models import BooleanField, IntegerField, TextField


class Template(models.Model):
    index = IntegerField(null=False, default=99999)
    code = TextField(null=False, unique=True)
    name = TextField(null=False)
    category = TextField(null=False)
    feature_code = TextField(null=False)
    type = TextField(null=False)
    description = TextField(null=True)
    enable = BooleanField(default=True)
    backend = TextField(default='common', null=False)
    display = BooleanField(default=True)
    subtemplate = TextField(null=True)
    location = TextField(null=False)
    params = TextField(null=True)
