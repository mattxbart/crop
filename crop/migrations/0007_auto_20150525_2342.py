# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0006_remove_amendment_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmendmentRatio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gypsum', models.FloatField()),
                ('manure', models.FloatField()),
                ('sulfur', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='amendment',
            name='ratio',
            field=models.ForeignKey(to='crop.AmendmentRatio', null=True),
        ),
    ]
