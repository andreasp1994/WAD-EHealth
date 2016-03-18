# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0002_category_shared'),
    ]

    operations = [
        migrations.AddField(
            model_name='searcher',
            name='email',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='searcher',
            name='name',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='searcher',
            name='surname',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='searcher',
            name='username',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
    ]
