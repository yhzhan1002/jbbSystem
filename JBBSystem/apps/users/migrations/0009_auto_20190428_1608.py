# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-28 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190428_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_vip',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='category',
            field=models.IntegerField(default=0, verbose_name='会员信息'),
        ),
    ]
