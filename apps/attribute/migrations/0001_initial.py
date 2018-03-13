# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-22 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Attribute',
                'ordering': ('title',),
                'verbose_name_plural': 'Attributes',
            },
        ),
        migrations.CreateModel(
            name='EntityAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Title')),
                ('attributes', models.ManyToManyField(to='attribute.Attribute')),
            ],
            options={
                'verbose_name': 'Entity attribute',
                'ordering': ('title',),
                'verbose_name_plural': 'Entity attributes',
            },
        ),
    ]
