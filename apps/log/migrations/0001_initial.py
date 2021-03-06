# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 09:42
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
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, verbose_name='IP')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='ДатаВремя')),
                ('query', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='JSON запрос')),
                ('event', models.CharField(max_length=100, verbose_name='Событие')),
                ('method', models.CharField(default='GET', max_length=100, verbose_name='Method')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
    ]
