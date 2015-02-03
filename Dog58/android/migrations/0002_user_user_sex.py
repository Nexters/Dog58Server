# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_sex',
            field=models.CharField(default='M', max_length=2),
            preserve_default=False,
        ),
    ]
