# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 08:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KumpulanDokumen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_dokumen', models.TextField(verbose_name='Nama dokumen')),
                ('kategori_dokumen', models.CharField(max_length=100, verbose_name='Kategori dokumen')),
                ('url_dokumen', models.TextField(validators=[django.core.validators.URLValidator()], verbose_name='URL dokumen')),
            ],
        ),
    ]
