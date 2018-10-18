# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-18 09:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0049_auto_20181003_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Classroom'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='custom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account'),
        ),
    ]
