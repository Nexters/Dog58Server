# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('user_age', models.IntegerField()),
                ('first_date', models.DateTimeField(auto_now_add=True)),
                ('last_date', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('push_cnt', models.IntegerField(default=0)),
                ('board', models.ManyToManyField(to='board.Board', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
