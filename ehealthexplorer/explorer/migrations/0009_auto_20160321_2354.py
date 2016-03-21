# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0008_auto_20160321_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searcher',
            name='email',
        ),
        migrations.RemoveField(
            model_name='searcher',
            name='name',
        ),
        migrations.RemoveField(
            model_name='searcher',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='searcher',
            name='username',
        ),
        migrations.AlterField(
            model_name='searcher',
            name='picture',
            field=models.CharField(default=b'/static/profile_images/default.png', max_length=100),
        ),
    ]
