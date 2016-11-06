# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0002_auto_20161105_1425'),
        ('reactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagereaction',
            name='allowed_reaction',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='imagereaction',
            name='episode',
            field=models.ForeignKey(to='episodes.Episode', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='imagereaction',
            name='username',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='tweetreaction',
            name='allowed_reaction',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tweetreaction',
            name='episode',
            field=models.ForeignKey(to='episodes.Episode', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tweetreaction',
            name='username',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='imagereaction',
            name='image',
            field=models.ImageField(upload_to='static/images', blank=True),
        ),
    ]
