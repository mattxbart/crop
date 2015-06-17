# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0011_almond'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alfalfa',
            name='cut_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='alfalfa',
            name='cutting',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='alfalfa',
            name='harvest_method',
            field=models.ForeignKey(blank=True, to='crop.HarvestMethod', null=True),
        ),
        migrations.AlterField(
            model_name='corn',
            name='seeds',
            field=models.FloatField(help_text=b'lbs. per acre', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crop',
            name='crop_yield',
            field=models.FloatField(null=True, verbose_name=b'Total Yield - tons', blank=True),
        ),
        migrations.AlterField(
            model_name='crop',
            name='moisture',
            field=models.FloatField(help_text=b'Moisture - pct.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crop',
            name='plant_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='milo',
            name='kernels',
            field=models.FloatField(help_text=b'lbs. per acre', null=True, blank=True),
        ),
    ]
