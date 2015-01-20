# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20150120_0348'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='board',
            name='content',
            field=ckeditor.fields.RichTextField(default=datetime.datetime(2015, 1, 19, 19, 42, 16, 306000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
