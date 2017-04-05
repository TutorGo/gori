# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 09:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0004_auto_20170404_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]

