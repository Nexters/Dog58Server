# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_board_share_cnt'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=128)),
                ('user_age', models.IntegerField()),
                ('first_date', models.DateTimeField(auto_now_add=True)),
                ('last_date', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('push_cnt', models.IntegerField(default=0)),
                ('board', models.ManyToManyField(to='board.Board')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
