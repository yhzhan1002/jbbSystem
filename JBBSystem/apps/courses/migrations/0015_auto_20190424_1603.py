# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-24 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20190424_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('cg', '常规课'), ('zt', '主题课')], default='', max_length=20, verbose_name='课程类别'),
        ),
    ]
