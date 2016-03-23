from django.db import models
from django.core.validators import URLValidator


# Create your models here.
class KumpulanDokumen(models.Model):
    nama_dokumen = models.TextField(verbose_name='Nama dokumen')
    kategori_dokumen = models.CharField(verbose_name='Kategori dokumen', max_length=100)
    url_dokumen = models.TextField(verbose_name='URL dokumen', validators=[URLValidator()])

    def __str__(self):
        return self.nama_dokumen
