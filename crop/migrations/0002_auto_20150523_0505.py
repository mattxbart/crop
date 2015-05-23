# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cornmilo',
            options={'verbose_name_plural': 'Corn Milo'},
        ),
        migrations.AlterModelOptions(
            name='field',
            options={'ordering': ('name', 'number')},
        ),
        migrations.AddField(
            model_name='cornmilo',
            name='total_tons',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
