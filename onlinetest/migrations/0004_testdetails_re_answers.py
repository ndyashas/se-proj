# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-22 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0003_studentmark_re_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='testdetails',
            name='re_answers',
            field=models.CharField(default='EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', max_length=120),
        ),
    ]