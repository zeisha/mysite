# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-22 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.IntegerField(default=1)),
                ('posts_words', models.CharField(default='', max_length=1000)),
                ('score', models.IntegerField(default=0)),
                ('search', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField(default=1)),
                ('blog_id', models.IntegerField(default=1)),
                ('comment_id', models.IntegerField(default=1)),
                ('text', models.TextField()),
                ('dateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField(default=1)),
                ('blog_id', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(default=None)),
                ('text', models.TextField()),
                ('dateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
