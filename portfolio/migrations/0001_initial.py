# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='pictures/')),
            ],
        ),
    ]
