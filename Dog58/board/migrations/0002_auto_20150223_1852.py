# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='update_date',
            new_name='update_date_start',
        ),
        migrations.AddField(
            model_name='board',
            name='update_date_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 23, 18, 52, 28, 320000)),
            preserve_default=False,
        ),
    ]
