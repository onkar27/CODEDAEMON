# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='clgname',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='experience',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
