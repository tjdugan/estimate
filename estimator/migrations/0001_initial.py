# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=220)),
                ('materialType', models.CharField(max_length=50)),
                ('footagePerUnit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('costPerUnit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('manufacturer', models.CharField(max_length=50)),
                ('dataSheetURL', models.CharField(max_length=200)),
                ('sdsURL', models.CharField(max_length=200)),
                ('distributor', models.CharField(max_length=220)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
