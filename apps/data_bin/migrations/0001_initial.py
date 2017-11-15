# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 10:28
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BinItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='query')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='data')),
                ('mapping', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='mapping')),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_bin.Bin')),
            ],
            options={
                'verbose_name_plural': 'Bin Items',
                'verbose_name': 'Bin Item',
            },
        ),
    ]