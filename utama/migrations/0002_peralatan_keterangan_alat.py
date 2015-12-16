# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utama', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peralatan',
            name='keterangan_alat',
            field=models.TextField(default=None, blank=True, verbose_name='Keterangan alat'),
        ),
    ]
