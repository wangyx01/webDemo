# Generated by Django 2.2 on 2019-04-25 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boxes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('number', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ch_name', models.CharField(max_length=10)),
                ('en_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=36)),
                ('Phone', models.CharField(max_length=36)),
                ('email', models.CharField(max_length=100)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mytest.Boxes')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mytest.Cities')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mytest.Departments')),
            ],
        )
    ]
