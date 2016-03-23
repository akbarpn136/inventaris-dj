from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='reformasi_halaman_utama'),
]
