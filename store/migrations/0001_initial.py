# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-24 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desription', models.TextField()),
                ('price', models.FloatField()),
                ('in_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='basket',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.User'),
        ),
    ]