# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0003_productionrate_production'),
    ]

    operations = [
        migrations.CreateModel(
            name='Architect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('website', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('website', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='ContractorRep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=35)),
                ('officenumber', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('website', models.CharField(max_length=220)),
                ('salesRep', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('website', models.CharField(max_length=220)),
                ('productRep', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ProductRep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=35)),
                ('officenumber', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='SalesRep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=35)),
                ('officenumber', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=55)),
            ],
        ),
    ]
