# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-24 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_basket_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.FileField(default='', upload_to=store.models.file_save_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
