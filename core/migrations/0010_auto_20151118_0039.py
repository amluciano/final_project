# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_post_visibility'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='visibility',
            new_name='category',
        ),
    ]
