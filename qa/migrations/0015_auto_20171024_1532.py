# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-24 10:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qa', '0014_auto_20171024_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('website', models.URLField(default='')),
                ('phone', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('order_byPhone', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='userqaprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserQAProfile',
        ),
    ]
