# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-27 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0015_problem_s_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reverse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=250)),
                ('p_level', models.CharField(max_length=250)),
                ('p_disc', models.TextField()),
                ('p_input', models.CharField(max_length=250)),
                ('p_cons', models.CharField(max_length=250)),
                ('p_output', models.CharField(max_length=250)),
                ('sample_input', models.TextField()),
                ('sample_output', models.TextField()),
                ('code', models.FileField(upload_to=b'')),
                ('success_sub', models.IntegerField(default=0)),
                ('tot_sub', models.IntegerField(default=0)),
                ('score', models.IntegerField()),
                ('s_rate', models.CharField(max_length=6)),
                ('Contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Contest')),
            ],
        ),
    ]
