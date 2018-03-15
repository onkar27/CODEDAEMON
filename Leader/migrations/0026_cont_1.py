# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 05:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Leader', '0025_auto_20170719_0508'),
    ]

    operations = [
        migrations.CreateModel(
            name='cont_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_time', models.TimeField(auto_now=True)),
                ('tot_score', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Leader.User')),
            ],
            options={
                'ordering': ['-tot_score', 'sub_time'],
            },
        ),
    ]
