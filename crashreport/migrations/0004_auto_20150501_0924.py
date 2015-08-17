# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crashreport', '0003_auto_20150401_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='crashreport',
            name='app_package',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crashreport',
            name='app_version_name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crashreport',
            name='app_verson_code',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crashreport',
            name='device_model',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crashreport',
            name='log_cat',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crashreport',
            name='product',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
