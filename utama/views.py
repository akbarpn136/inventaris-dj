from django.shortcuts import render
from .models import Peralatan


# Create your views here.
def utama(request):
    data_alat = Peralatan.objects.select_related().order_by('ruang_alat')
    data_komputer = Peralatan.objects.filter(kategori_alat__nama_kategori='Komputer')
    data_printer = Peralatan.objects.filter(kategori_alat__nama_kategori='Printer')

    data_komputer_rusak = data_komputer.filter(kondisi_alat=False)
    data_printer_rusak = data_printer.filter(kondisi_alat=False)

    data = {
        'Peralatan': data_alat,
        'komputer': data_komputer,
        'printer': data_printer,
        'komputer_rusak': data_komputer_rusak,
        'printer_rusak': data_printer_rusak,
    }

    return render(request, 'utama/daftar_peralatan.html', data)
