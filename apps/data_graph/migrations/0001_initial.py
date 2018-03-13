# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 21:23
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
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
            name='Graph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Graph',
                'verbose_name_plural': 'Graph list',
            },
        ),
        migrations.CreateModel(
            name='GraphData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='data')),
                ('graph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_graph.Graph')),
            ],
            options={
                'verbose_name': 'Graph data row',
                'verbose_name_plural': 'Graph data',
            },
        ),
        migrations.CreateModel(
            name='GraphModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('fields', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('is_group', models.BooleanField(default=False, verbose_name='Is group')),
            ],
            options={
                'verbose_name': 'Graph model',
                'verbose_name_plural': 'Graph models',
            },
        ),
        migrations.CreateModel(
            name='GraphModelDrawing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(null=True, verbose_name='json')),
            ],
            options={
                'verbose_name': 'Graph model drawing',
                'verbose_name_plural': 'Graph model drawings',
            },
        ),
        migrations.CreateModel(
            name='GraphNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_json', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Node json')),
                ('graph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_graph.Graph')),
            ],
        ),
        migrations.CreateModel(
            name='GraphNodeEdge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edge_json', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Edge json')),
                ('graph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_graph.Graph')),
            ],
        ),
        migrations.CreateModel(
            name='GraphRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('from_fields', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('to_fields', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('comparators', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('equal', 'equal'), ('similar', 'similar'), ('translit_similar', 'translit_similar')], default='equal', max_length=50), help_text="choose from 'equal, similar, translit_similar', write without whitespaces", size=None)),
                ('graph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_graph.Graph')),
            ],
            options={
                'verbose_name': 'Graph relation',
                'verbose_name_plural': 'Graph relations',
            },
        ),
        migrations.AddField(
            model_name='graphmodel',
            name='drawing',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_graph.GraphModelDrawing'),
        ),
        migrations.AddField(
            model_name='graphmodel',
            name='graph',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_graph.Graph'),
        ),
    ]
