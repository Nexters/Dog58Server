# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20150120_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='title_img',
            field=models.ImageField(upload_to=b''),
            preserve_default=True,
        ),
    ]
