# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20150223_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='thumbnail',
            field=models.ImageField(upload_to=b'./uploads/thumbnails/', null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
