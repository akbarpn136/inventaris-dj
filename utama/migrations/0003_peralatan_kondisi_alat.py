# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utama', '0002_peralatan_keterangan_alat'),
    ]

    operations = [
        migrations.AddField(
            model_name='peralatan',
            name='kondisi_alat',
            field=models.BooleanField(default=False, verbose_name='Kondisi Peralatan'),
        ),
    ]
