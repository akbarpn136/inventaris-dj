from django.shortcuts import render

from .models import KumpulanDokumen


# Create your views here.
def index(request):
    data_dokumen = KumpulanDokumen.objects.all()
    data = {
        'dokumen': data_dokumen
    }

    return render(request, 'reformasi/daftar_reformasi.html', data)
