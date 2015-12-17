# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utama', '0003_peralatan_kondisi_alat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peralatan',
            name='kondisi_alat',
            field=models.BooleanField(verbose_name='Kondisi Peralatan', default=True),
        ),
    ]
