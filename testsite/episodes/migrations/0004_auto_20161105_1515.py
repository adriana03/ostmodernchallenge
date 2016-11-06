# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0003_auto_20161105_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='hero_image',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
    ]
