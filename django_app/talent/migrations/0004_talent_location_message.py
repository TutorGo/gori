# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0002_location_location_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='location_message',
            field=models.TextField(blank=True),
        ),
    ]
