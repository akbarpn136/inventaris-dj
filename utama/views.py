from django.shortcuts import render
from .models import Peralatan


# Create your views here.
def utama(request):
    data_alat = Peralatan.objects.select_related().order_by('-kategori_alat')
    return render(request, 'utama/daftar_peralatan.html', {'Peralatan': data_alat})
