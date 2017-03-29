# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 07:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('talent', '0007_auto_20170328_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='is_registered',
            new_name='is_confirmed',
        ),
        migrations.AddField(
            model_name='registration',
            name='class_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='talent.Location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='experience_length',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='registration',
            name='message_to_tutor',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='student_level',
            field=models.IntegerField(choices=[(1, '입문자'), (2, '초/중급자'), (3, '상급자')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talent',
            name='student',
            field=models.ManyToManyField(through='talent.Registration', to=settings.AUTH_USER_MODEL),
        ),
    ]