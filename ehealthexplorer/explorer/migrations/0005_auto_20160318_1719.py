# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0004_category_time_shared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
