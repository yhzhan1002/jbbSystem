# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-28 16:57
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_usertimetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertimetable',
            name='timetable',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='课表'),
        ),
    ]
