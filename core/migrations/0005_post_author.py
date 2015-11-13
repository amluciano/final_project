# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151105_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=datetime.datetime(2015, 11, 13, 13, 15, 39, 571515, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
    ]
