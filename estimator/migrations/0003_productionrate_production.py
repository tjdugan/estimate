# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0002_productionrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionrate',
            name='production',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
    ]
