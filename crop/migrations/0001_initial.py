# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alfalfa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plant_date', models.DateField()),
                ('harvest_date', models.DateField(null=True, blank=True)),
                ('crop_yield', models.FloatField(help_text=b'tons')),
                ('moisture', models.FloatField(help_text=b'pct.')),
                ('cutting', models.PositiveIntegerField()),
                ('cut_date', models.DateField()),
                ('pickup_date', models.DateField(null=True, blank=True)),
                ('weed_spray', models.DateField(null=True, blank=True)),
                ('first_water', models.DateField(null=True, blank=True)),
                ('second_water', models.DateField(null=True, blank=True)),
                ('total_tons', models.FloatField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Amendment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('customer', models.PositiveIntegerField()),
                ('date_applied', models.DateField()),
                ('tons', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='AmendmentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CornMilo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plant_date', models.DateField()),
                ('harvest_date', models.DateField(null=True, blank=True)),
                ('crop_yield', models.FloatField(help_text=b'tons')),
                ('moisture', models.FloatField(help_text=b'pct.')),
                ('seeds', models.FloatField(help_text=b'lbs. per acre')),
                ('kernels', models.FloatField(help_text=b'lbs. per acre')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CropType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('variety', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('acres', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HarvestMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='cornmilo',
            name='field',
            field=models.ForeignKey(to='crop.Field'),
        ),
        migrations.AddField(
            model_name='cornmilo',
            name='type',
            field=models.ForeignKey(to='crop.CropType'),
        ),
        migrations.AddField(
            model_name='amendment',
            name='amendment_type',
            field=models.ForeignKey(to='crop.AmendmentType'),
        ),
        migrations.AddField(
            model_name='amendment',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='alfalfa',
            name='field',
            field=models.ForeignKey(to='crop.Field'),
        ),
        migrations.AddField(
            model_name='alfalfa',
            name='harvest_method',
            field=models.ForeignKey(to='crop.HarvestMethod'),
        ),
        migrations.AddField(
            model_name='alfalfa',
            name='type',
            field=models.ForeignKey(to='crop.CropType'),
        ),
    ]
