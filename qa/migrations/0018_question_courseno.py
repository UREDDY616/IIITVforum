# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-30 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('qa', '0017_auto_20171025_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='courseNo',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='student.Courses'),
        ),
    ]
