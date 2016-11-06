# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='hero_image',
            field=models.ImageField(upload_to='/images/', blank=True),
        ),
    ]
