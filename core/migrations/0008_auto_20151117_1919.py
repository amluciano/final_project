# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20151117_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rating',
        ),
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=0, choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')]),
        ),
    ]
