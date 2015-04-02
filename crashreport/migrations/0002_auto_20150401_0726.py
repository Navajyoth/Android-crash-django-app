# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crashreport', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crashreport',
            name='crash_id',
        ),
        migrations.AlterField(
            model_name='crashreport',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
