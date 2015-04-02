# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crashreport', '0002_auto_20150401_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='crashreport',
            name='android_ver',
            field=models.CharField(default='2.3', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crashreport',
            name='brand',
            field=models.CharField(default='samsung', max_length=100),
            preserve_default=False,
        ),
    ]
