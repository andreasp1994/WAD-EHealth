# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0008_auto_20160321_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searcher',
            name='picture',
            field=models.ImageField(default=b'/static/prof-img/user.png', upload_to=b'profile_images'),
        ),
    ]
