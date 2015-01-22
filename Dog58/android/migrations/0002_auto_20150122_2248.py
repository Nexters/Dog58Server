# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='board',
            field=models.ManyToManyField(to='board.Board', null=True, blank=True),
            preserve_default=True,
        ),
    ]
