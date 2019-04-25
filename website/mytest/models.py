from django.db import models
from django.db.models import (
    IntegerField, TextField, CharField, ForeignKey
)


class Cities(models.Model):
    ch_name = CharField(max_length=10, null=False)
    en_name = CharField(max_length=10, null=False)


class Departments(models.Model):
    name = CharField(max_length=10, null=False)
    description = TextField(null=False)


class Boxes(models.Model):
    type = CharField(max_length=10, null=False)
    price = IntegerField(null=False)
    number = CharField(max_length=32, null=False)


class Employees(models.Model):
    city = ForeignKey(Cities, null=False, on_delete=models.CASCADE)
    department = ForeignKey(Departments, null=False, on_delete=models.CASCADE)
    box = ForeignKey(Boxes, null=False, on_delete=models.CASCADE)
    employee_id = CharField(max_length=10)
    name = CharField(max_length=36)
    Phone = CharField(max_length=36)
    email = CharField(max_length=100)
