# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20150120_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='title_img',
            field=models.ImageField(upload_to=b'./uploads/title/'),
            preserve_default=True,
        ),
    ]
