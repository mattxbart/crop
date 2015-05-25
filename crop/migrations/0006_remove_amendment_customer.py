# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0005_auto_20150525_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amendment',
            name='customer',
        ),
    ]
