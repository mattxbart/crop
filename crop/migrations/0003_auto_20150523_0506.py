# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0002_auto_20150523_0505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alfalfa',
            name='total_tons',
        ),
        migrations.RemoveField(
            model_name='cornmilo',
            name='total_tons',
        ),
    ]
