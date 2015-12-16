# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nama_kategori', models.CharField(verbose_name='Kategori', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Peralatan',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nama_alat', models.CharField(verbose_name='Tipe/Merk', max_length=200)),
                ('ip_alat', models.GenericIPAddressField(null=True, blank=True, verbose_name='IP')),
                ('kategori_alat', models.ForeignKey(to='utama.Kategori')),
                ('personal_alat', models.ForeignKey(verbose_name='Penanggung Jawab', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ruangan',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nama_ruang', models.CharField(verbose_name='Nama Ruangan', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='peralatan',
            name='ruang_alat',
            field=models.ForeignKey(to='utama.Ruangan'),
        ),
    ]
