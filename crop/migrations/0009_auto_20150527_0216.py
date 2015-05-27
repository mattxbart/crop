# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0008_auto_20150525_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plant_date', models.DateField()),
                ('harvest_date', models.DateField(null=True, blank=True)),
                ('crop_yield', models.FloatField(verbose_name=b'Total Yield - tons')),
                ('moisture', models.FloatField(help_text=b'Moisture - pct.')),
                ('field', models.ForeignKey(to='crop.Field')),
                ('type', models.ForeignKey(to='crop.CropType')),
            ],
        ),
        migrations.RemoveField(
            model_name='alfalfa',
            name='crop_yield',
        ),
        migrations.RemoveField(
            model_name='alfalfa',
            name='field',
        ),
        migrations.RemoveField(
            model_name='alfalfa',
            name='harvest_date',
        ),
        migrations.RemoveField(
            model_name='alfalfa',
            name='id',
        ),
        migrations.RemoveField(
            model_name='alfalfa',
            name='moisture',
        ),
        migrations.RemoveField(
            model_name='alfalfa',
            name='plant_date',
        ),
        migrations.RemoveField(
            model_name='alfalfa',
            name='type',
        ),
        migrations.RemoveField(
            model_name='cornmilo',
            name='crop_yield',
        ),
        migrations.RemoveField(
            model_name='cornmilo',
            name='field',
        ),
        migrations.RemoveField(
            model_name='cornmilo',
            name='harvest_date',
        ),
        migrations.RemoveField(
            model_name='cornmilo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cornmilo',
            name='moisture',
        ),
        migrations.RemoveField(
            model_name='cornmilo',
            name='plant_date',
        ),
        migrations.RemoveField(
            model_name='cornmilo',
            name='type',
        ),
        migrations.AddField(
            model_name='alfalfa',
            name='crop_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='crop.Crop'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cornmilo',
            name='crop_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='crop.Crop'),
            preserve_default=False,
        ),
    ]
