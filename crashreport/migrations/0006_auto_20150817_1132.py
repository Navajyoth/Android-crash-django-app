# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crashreport', '0005_auto_20150501_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crashreport',
            name='android_ver',
            field=models.CharField(max_length=10000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crashreport',
            name='app_package',
            field=models.CharField(max_length=10000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crashreport',
            name='app_start_date',
            field=models.CharField(max_length=10000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crashreport',
            name='app_version_name',
            field=models.CharField(max_length=10000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crashreport',
            name='app_verson_code',
            field=models.CharField(max_length=10000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crashreport',
            name='available_memory',
            field=models.CharField(max_length=10000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crashreport',
            name='brand',
            field=models.CharField(max_length=10000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crashreport',
            name='crash_date',
            field=models.CharField(max_length=10000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crashreport',
            name='device_model',
            field=models.CharField(max_length=10000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crashreport',
            name='product',
            field=models.CharField(max_length=10000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crashreport',
            name='shared_pref',
            field=models.CharField(max_length=10000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crashreport',
            name='total_memory',
            field=models.CharField(max_length=10000, null=True),
            preserve_default=True,
        ),
    ]
