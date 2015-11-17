# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20151117_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visibility',
            field=models.IntegerField(default=0, choices=[(0, b'Fiction'), (1, b'Mystery & Crime'), (2, b'Poetry'), (3, b'Romance'), (4, b'Science Fiction'), (5, b'Thrillers'), (6, b'Childrens'), (7, b'Nonfiction')]),
        ),
    ]
