# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0007_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='flesch_score',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='page',
            name='polarity_score',
            field=models.DecimalField(default=0.0, max_digits=3, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='page',
            name='subjectivity_score',
            field=models.DecimalField(default=0.0, max_digits=3, decimal_places=2),
        ),
    ]
