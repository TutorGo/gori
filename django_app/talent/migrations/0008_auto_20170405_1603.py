# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0007_merge_20170405_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='curriculum_rate',
            new_name='curriculum',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='delivery_rate',
            new_name='delivery',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='friendliness_rate',
            new_name='friendliness',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='readiness_rate',
            new_name='readiness',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='timeliness_rate',
            new_name='timeliness',
        ),
    ]
