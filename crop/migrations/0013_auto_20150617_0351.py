# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0012_auto_20150617_0345'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AmendmentRatio',
            new_name='ApplicationRate',
        ),
        migrations.RenameField(
            model_name='amendment',
            old_name='amendment_ratio',
            new_name='application_rate',
        ),
    ]
