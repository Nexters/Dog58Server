# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('title_img', models.ImageField(upload_to=b'./uploads/title/')),
                ('content', ckeditor.fields.RichTextField()),
                ('register_date', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('update_date', models.DateTimeField()),
                ('share_cnt', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
