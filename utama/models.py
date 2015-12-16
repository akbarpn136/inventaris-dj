from django.db import models


# Create your models here.
class Ruangan(models.Model):
    nama_ruang = models.CharField(max_length=100, verbose_name='Nama Ruangan')

    def __str__(self):
        return self.nama_ruang


class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=200, verbose_name='Kategori')

    def __str__(self):
        return self.nama_kategori


class Peralatan(models.Model):
    nama_alat = models.CharField(max_length=200, verbose_name='Tipe/Merk')
    ip_alat = models.GenericIPAddressField(verbose_name='IP', blank=True, null=True)
    keterangan_alat = models.TextField(verbose_name='Keterangan alat', blank=True, default=None)
    personal_alat = models.ForeignKey('auth.User', verbose_name='Penanggung Jawab')
    kategori_alat = models.ForeignKey(Kategori)
    ruang_alat = models.ForeignKey(Ruangan)
