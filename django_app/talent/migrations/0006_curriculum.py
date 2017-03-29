# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0005_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('talent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talent.Talent')),
            ],
        ),
    ]