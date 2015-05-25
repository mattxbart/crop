# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0007_auto_20150525_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amendment',
            name='amendment_type',
        ),
        migrations.RemoveField(
            model_name='amendment',
            name='ratio',
        ),
        migrations.AddField(
            model_name='amendment',
            name='amendment_ratio',
            field=models.ForeignKey(default=1, to='crop.AmendmentRatio'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AmendmentType',
        ),
    ]
