# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('cognome', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=10)),
                ('indirizzo', models.CharField(max_length=30)),
            ],
        ),
    ]
