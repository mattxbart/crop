# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0010_auto_20150527_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almond',
            fields=[
                ('crop_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='crop.Crop')),
            ],
            bases=('crop.crop',),
        ),
    ]
