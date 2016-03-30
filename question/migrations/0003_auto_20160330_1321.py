# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20160330_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='question.Category'),
        ),
    ]
