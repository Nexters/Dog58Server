# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='board',
            field=models.ManyToManyField(to='board.Board', null=True, blank=True),
            preserve_default=True,
        ),
    ]
