# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-07 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.FileField(default='under_construction.html', upload_to='projects/'),
        ),
    ]
