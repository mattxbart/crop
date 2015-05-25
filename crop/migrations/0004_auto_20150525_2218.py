# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0003_auto_20150523_0506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cornmilo',
            options={'verbose_name_plural': 'Corn & Milo'},
        ),
        migrations.RenameField(
            model_name='amendment',
            old_name='object_id',
            new_name='crop_id',
        ),
        migrations.RenameField(
            model_name='amendment',
            old_name='content_type',
            new_name='crop_type',
        ),
        migrations.AlterField(
            model_name='alfalfa',
            name='crop_yield',
            field=models.FloatField(verbose_name=b'Total Yield - tons'),
        ),
        migrations.AlterField(
            model_name='alfalfa',
            name='moisture',
            field=models.FloatField(help_text=b'Moisture - pct.'),
        ),
        migrations.AlterField(
            model_name='cornmilo',
            name='crop_yield',
            field=models.FloatField(verbose_name=b'Total Yield - tons'),
        ),
        migrations.AlterField(
            model_name='cornmilo',
            name='moisture',
            field=models.FloatField(help_text=b'Moisture - pct.'),
        ),
        migrations.AlterField(
            model_name='field',
            name='number',
            field=models.CharField(max_length=255, verbose_name=b'Field Number'),
        ),
    ]
