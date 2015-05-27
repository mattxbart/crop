# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0009_auto_20150527_0216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corn',
            fields=[
                ('crop_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='crop.Crop')),
                ('seeds', models.FloatField(help_text=b'lbs. per acre')),
            ],
            options={
                'verbose_name_plural': 'Corn',
            },
            bases=('crop.crop',),
        ),
        migrations.CreateModel(
            name='Milo',
            fields=[
                ('crop_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='crop.Crop')),
                ('kernels', models.FloatField(help_text=b'lbs. per acre')),
            ],
            options={
                'verbose_name_plural': 'Milo',
            },
            bases=('crop.crop',),
        ),
        migrations.RemoveField(
            model_name='cornmilo',
            name='crop_ptr',
        ),
        migrations.DeleteModel(
            name='CornMilo',
        ),
    ]
