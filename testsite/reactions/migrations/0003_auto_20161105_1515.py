# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactions', '0002_auto_20161105_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagereaction',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
    ]
