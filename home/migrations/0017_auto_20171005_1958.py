# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-05 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_problem_r_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='p_input',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='problem',
            name='p_output',
            field=models.TextField(),
        ),
    ]
